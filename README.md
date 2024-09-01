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

