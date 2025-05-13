# Enter the code here

# Joshua Koroma
class attack_value:
    def __init__(self, attack_value):
        self.attack_value = attack_value

def type_interactions():
# The goal of this function is to define the five types used in this game, as 
# well as how one type attacking another would lead either to 
# neutral, more, or less damage being dealt. Every fighter must be assigned a type.

    type_interactions = ""

    # These are the five types, with each fighter needing one to be assigned to them
    attacker_types = ["Purple", "Green", "Blue", "Red", "Yellow"]

    # The five types a victim could be.

    victim_types = ["Purple", "Green", "Blue", "Red", "Yellow"]

    # The basic type of interaction that happens in the game. At times, the enemy will be the victim and the player will be the attacker, and vice versa

    interactions = {attacker_types:victim_types}

    # This is a list of dictionaries about what counts as a Super effective interaction, using the attacker's type as a key and the victim's type as a value
    super_effective = [ {"Purple":"Green"},
                         {"Green":"Blue"},
                         {"Blue":"Red"},
                         {"Red":"Yellow"},
                         {"Yellow":"Purple"} ]
    
    # List of dictionaries about ineffective interactions, using the same attacker:victim rules as above
    ineffective = [ {"Green": "Purple"}, 
                   {"Purple": "Yellow"}, 
                   {"Yellow": "Red"}, 
                   {"Red": "Blue"},
                   {"Blue": "Green"} ]
    
    # Iterates through the super_effective dictionary to find a match between attacker and 
    for attack in super_effective:
        if super_effective is True:
            (attack_value * 1.3)

        elif ineffective is True:
            (attack_value * 0.7)

        else:
            (attack_value * 1)
    return type_interactions

# Aaryan Batra
def get_fighter_options():
    options = ["Fighter 1 (Green)", "Fighter 2 (Green)", "Fighter 3 (Blue)", "Fighter 4 (Blue)", "Fighter 5 (Red)", 
               "Fighter 6 (Red)", "Fighter 7 (Purple)", "Fighter 8 (Purple)", "Fighter 9 (Yellow)", "Fighter 10 (Yellow)"]
    
    print("Select 5 options from the list:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    return options


def select_options():
    """
    User input and validation for selecting 5 fighters.
    """
    options = get_fighter_options()
    selected = []
    selection = False
    
    while not selection:
        print("\nEnter 5 numbers between 1-10, separated by spaces:")
        user_input = input("> ")
        choices = user_input.split()        

        if len(choices) != 5:
            print(f"Please select exactly 5 options. You entered {len(choices)}.")
            continue
        
        valid_numbers = True
        numbers = []
        for choice in choices:
            if not choice.isdigit():
                valid_numbers = False
                break
            numbers.append(int(choice))
        
        if not valid_numbers:
            print("Please enter only numbers.")
            continue     

        if any(num < 1 or num > 10 for num in numbers):
            print("All numbers must be between 1 and 10.")
            continue
        
        if len(set(numbers)) != 5:
            print("Please select 5 different options (no duplicates).")
            continue
        
        selected = [options[num-1] for num in numbers]
        selection = True

    print("\nYour selections:")
    for option in selected:
        print(f"- {option}")
    
    return selected


if __name__ == "__main__":
    select_options()

# Mehret Berihun

import random

def run_game(team, enemy_health=100, team_health=100):
    """
    Simulates a battle between the player's team and an enemy.

    Parameters:
    team (list): List of monster names.
    enemy_health (int): Starting health of the enemy.
    team_health (int): Collective health of the team.

    Returns:
    None
    """
    print("\n--- Battle Start! ---")
    damage_tracker = {monster: 0 for monster in team}

    round_number = 1
    while enemy_health > 0 and team_health > 0:
        print(f"\n--- Round {round_number} ---")
        for monster in team:
            if enemy_health <= 0:
                break
            # Simulate damage (can be replaced with type-based calc later)
            damage = random.randint(5, 20)
            print(f"{monster} attacks the enemy for {damage} damage!")
            enemy_health -= damage
            damage_tracker[monster] += damage

            # Optional: Simulate enemy hitting back
            retaliation = random.randint(3, 10)
            print(f"Enemy hits back for {retaliation} damage!")
            team_health -= retaliation

            print(f"Enemy Health: {max(enemy_health, 0)}")
            print(f"Team Health: {max(team_health, 0)}")

            if team_health <= 0:
                break
        
        round_number += 1

    # Outcome
    if enemy_health <= 0:
        print("\nYou won the battle!")
        total_xp = 100  # Arbitrary XP value for a win
        xp_distribution = distribute_experience(total_xp, damage_tracker)
        print("XP Distribution:")
        for monster, xp in xp_distribution.items():
            print(f"{monster}: {xp} XP")
    else:
        print("\nYou lost the battle!")


# Adithya Menon
def level_up_fighters(fighter_xp, current_levels):
    level_ups = {}
    
    # XP thresholds for each level (e.g., level 2 requires 100 XP, level 3 requires 250 XP, etc.)
    xp_thresholds = {
        1: 0,
        2: 100,
        3: 250,
        4: 450,
        5: 700,
        6: 1000,
        7: 1350,
        8: 1750,
        9: 2200,
        10: 2700
    }
    
    for fighter, xp in fighter_xp.items():
        current_level = current_levels.get(fighter, 1)
        
        # Find the highest level the fighter qualifies for
        new_level = current_level
        for level, threshold in xp_thresholds.items():
            if xp >= threshold and level > new_level:
                new_level = level
        
        # Record level up if applicable
        if new_level > current_level:
            level_ups[fighter] = new_level
    
    return level_ups

def calculate_stats(fighter_name, fighter_level):
    """
    Calculates a fighter's stats based on their level and type.
    
    Parameters:
    fighter_name (str): Name of the fighter including type (e.g., "Fighter 1 (Green)")
    fighter_level (int): Current level of the fighter
    
    Returns:
    dict: Dictionary containing the fighter's stats
    """
    # Extract fighter type from name
    fighter_type = fighter_name.split("(")[1].strip(")")
    
    # Base stats for level 1
    base_stats = {
        "health": 50,
        "attack": 10,
        "defense": 8,
        "speed": 7
    }
    
    # Type-specific stat modifiers
    type_modifiers = {
        "Purple": {"health": 1.2, "attack": 0.9, "defense": 1.1, "speed": 0.8},
        "Green": {"health": 1.3, "attack": 0.8, "defense": 1.2, "speed": 0.7},
        "Blue": {"health": 0.9, "attack": 1.0, "defense": 0.9, "speed": 1.2},
        "Red": {"health": 0.8, "attack": 1.3, "defense": 0.7, "speed": 1.2},
        "Yellow": {"health": 1.0, "attack": 1.0, "defense": 1.0, "speed": 1.0}
    }
    
    # Calculate stats based on level and type
    stats = {}
    for stat, base_value in base_stats.items():
        # Apply level scaling (each level adds 5% to base stats)
        level_multiplier = 1 + (0.05 * (fighter_level - 1))
        
        # Apply type modifier
        type_multiplier = type_modifiers[fighter_type][stat]
        
        # Calculate final stat value
        stats[stat] = round(base_value * level_multiplier * type_multiplier)
    
    # Add level and type to stats dictionary
    stats["level"] = fighter_level
    stats["type"] = fighter_type
    
    return stats
