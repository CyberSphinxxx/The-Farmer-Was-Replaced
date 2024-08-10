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
