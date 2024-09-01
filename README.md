# The Farmer Was Replaced - Code Collection

This repository contains a collection of code snippets and solutions for the game "The Farmer Was Replaced!". The game involves coding drones to automate farming tasks, solve mazes, and manage crops. Below are descriptions of the different scripts included in this repository.

This repository is direct copy paste. You just need to copy the code you need then paste it in your in-game terminal to use it.

## Table of Contents

- [Maze Generator](#maze-generator)
- [Maze Solver](#maze-solver)
- [Pumpkin Management](#pumpkin-management)

## Maze Generator

The `Maze Generator` script is used to create a maze by planting bushes across the grid and applying fertilizer to transform bushes into hedges, forming a maze.

```python
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

def execute():
    plant_bushes_across_grid()
    maze_created = apply_fertilizer_to_bushes()
    if not maze_created:
        quick_print("No maze was created. Try again.")

# Start the process
execute()
```

## Maze Solver
The `Maze Solver` script is designed to navigate and solve a generated maze. It can handle various conditions, including finding treasure and avoiding obstacles.

```python
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
    # Logic to find the treasure within the maze
    pass

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
```

