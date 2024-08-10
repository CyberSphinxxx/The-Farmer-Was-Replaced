# Maze Generator
def plant_bushes_across_grid():
    world_size = get_world_size()
    for i in range(world_size):
        for j in range(world_size):
            move_to(i, j)
            if get_entity_type() != Entities.Bush:
                plant(Entities.Bush)

def apply_fertilizer_to_bushes():
    world_size = get_world_size()
    for i in range(world_size):
        for j in range(world_size):
            move_to(i, j)
            if get_entity_type() == Entities.Bush:
                if num_items(Items.Fertilizer) == 0:
                    trade(Items.Fertilizer)
                use_item(Items.Fertilizer)
                if get_entity_type() == Entities.Hedge:
                    quick_print("Maze created!")
                    return True
                else:
                    harvest()
    return False

# Maze Solver
def startMaze():
    clear()
    plant(Entities.Bush)
    while not is_over(Entities.Hedge) and not is_over(Entities.Treasure):
        useFertilizer()
    solveMaze()

def solveMaze():
    facing = 0
    directions = [North, East, South, West]

    while get_entity_type() != Entities.Treasure:
        x = get_pos_x()
        y = get_pos_y()

        move(directions[facing % 4])

        facing += 1
        if x == get_pos_x() and y == get_pos_y():
            facing += 2

    harvest()

def findTreasure():
    been = []
    path = [[get_pos_x(), get_pos_y()]]

    while True:
        if is_over(Entities.Treasure):
            harvest()
            break

        posX = get_pos_x()
        posY = get_pos_y()
        pos = [posX, posY]
        freedom = getBranching()
        moved = False

        for direction in freedom:
            dirpos = direction[1]
            pathContains = False
            beenContains = False

            for p in path:
                if (p[0] == dirpos[0]) and (p[1] == dirpos[1]):
                    pathContains = True
            for p in been:
                if (p[0] == dirpos[0]) and (p[1] == dirpos[1]):
                    beenContains = True

            if not beenContains and not pathContains:
                move(direction[0])
                path.append(pos)
                moved = True
                break
        if not moved:
            a = path.pop()
            if len(freedom) == 2:
                been.pop()
            been.append(pos)
            backtrack(a, posX, posY)

def getBranching():
    directions = [North, East, South, West]
    branching = []
    ind = 0
    for direction in directions:
        initX = get_pos_x()
        initY = get_pos_y()
        move(direction)
        newX = get_pos_x()
        newY = get_pos_y()
        wall = initX == newX and initY == newY
        if not wall:
            backInd = ind
            if ind >= 2:
                backInd -= 2
            else:
                backInd += 2
            move(directions[backInd])
            branching.append([direction, [newX, newY]])
        ind += 1
    return branching

def backtrack(route, x, y):
    if x > route[0]:
        move(West)
    elif x < route[0]:
        move(East)
    elif y > route[1]:
        move(South)
    elif y < route[1]:
        move(North)

# Main Loop: Generate, Solve, Repeat
while True:
    plant_bushes_across_grid()
    maze_created = apply_fertilizer_to_bushes()
    if maze_created:
        quick_print("Maze generated! Starting solver...")
        solveMaze()
        quick_print("Maze solved! Generating new maze...")
    else:
        quick_print("No maze was created. Trying again.")
    
