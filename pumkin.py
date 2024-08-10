from utils import move_to, move_back_direction, water_soil

def plant_pumpkin():
    if num_items(Items.Pumpkin_Seed) == 0:
        trade(Items.Pumpkin_Seed)
    if get_ground_type() == Grounds.Turf:
        till()
    if get_ground_type() == Grounds.Soil:
        water_soil()
    plant(Entities.Pumpkin)

def check_and_plant_pumpkin(tracked_positions):
    world_size = get_world_size()
    for i in range(world_size):
        for j in range(world_size):
            move_to(i, j)
            entity_type = get_entity_type()
            if entity_type != Entities.Pumpkin and entity_type != Entities.Treasure:
                plant_pumpkin()
                tracked_positions.append((i, j))

def replant_pumpkins(tracked_positions):
    new_tracked_positions = []
    for position in tracked_positions:
        i, j = position
        move_to(i, j)
        if get_entity_type() != Entities.Pumpkin:
            plant_pumpkin()
            new_tracked_positions.append((i, j))
    return new_tracked_positions

def is_field_filled_with_pumpkins():
    world_size = get_world_size()
    for i in range(world_size):
        for j in range(world_size):
            move_to(i, j)
            if get_entity_type() != Entities.Pumpkin:
                return False
    return True

def manage_pumpkin_field():
    tracked_positions = []
    check_and_plant_pumpkin(tracked_positions)
    quick_print("Initial planting complete.")
    quick_print("Tracking positions of replanted pumpkins.")

    while tracked_positions:
        tracked_positions = replant_pumpkins(tracked_positions)
        quick_print("Replanted pumpkins where necessary.")
        quick_print("Remaining positions to check:")
        quick_print(len(tracked_positions))
        # Optionally, you might want to wait for some time before checking again
        # This is to allow the pumpkins to grow and potentially die if you want to replant in waves
        # sleep(60)  # Example: wait for 60 seconds

# Start the infinite loop
while True:
    manage_pumpkin_field()

    # Harvesting once the field is filled with pumpkins
    if is_field_filled_with_pumpkins():
        quick_print("Field filled with pumpkins. Harvesting!")
        move_to(0, 0)  # Move to a known location to start harvesting
        if can_harvest():
            harvest()
    
    quick_print("Restarting the process...")

def move_to(x, y):
    while get_pos_x() != x or get_pos_y() != y:
        current_x = get_pos_x()
        current_y = get_pos_y()
        moved = False
        if current_x < x and move(East):
            moved = True
        elif current_x > x and move(West):
            moved = True
        elif current_y < y and move(North):
            moved = True
        elif current_y > y and move(South):
            moved = True
        
        # If no move was successful, break to avoid getting stuck
        if not moved:
            return False
    return True

def move_back_direction(direction):
    if direction == North:
        move(South)
    elif direction == South:
        move(North)
    elif direction == East:
        move(West)
    elif direction == West:
        move(East)

def move_back_position(original_position):
    current_x = get_pos_x()
    current_y = get_pos_y()
    original_x = original_position[0]
    original_y = original_position[1]

    if current_x < original_x:
        move(East)
    elif current_x > original_x:
        move(West)
    elif current_y < original_y:
        move(North)
    elif current_y > original_y:
        move(South)

def water_soil():
    # Constants
    TARGET_WATER_LEVEL = 0.5  # Adjusted to be more conservative
    TANK_CAPACITY = 0.25
    MIN_WATER_LEVEL = 0.2  # Water if below this level

    water_level = get_water()
    if water_level < MIN_WATER_LEVEL:
        needed_water = TARGET_WATER_LEVEL - water_level
        tanks_needed = needed_water / TANK_CAPACITY
        # Use tanks only up to a certain limit to conserve resources
        max_tanks_to_use = 5  # Adjust as necessary to balance water usage
        tanks_used = 0
        while tanks_used < tanks_needed and tanks_used < max_tanks_to_use:
            if num_items(Items.Water_Tank) > 0:
                use_item(Items.Water_Tank)
                tanks_used += 1
            else:
                break
    if num_items(Items.Empty_Tank) + num_items(Items.Water_Tank) < 100:
        trade(Items.Empty_Tank)
