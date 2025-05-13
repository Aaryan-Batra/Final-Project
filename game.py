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
def fighter_options():
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
    options = fighter_options()
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
  
def initialize_fighters():  
    # Create 10 fighters with predefined types and levels  
    fighters = ["Fighter" + str(i) for i in range(1, 11)]  
    types_list = ["Red", "Blue", "Green", "Purple", "Yellow"]  
    fighter_types = {fighter: types_list[(i % len(types_list))] for i, fighter in enumerate(fighters)}  
    fighter_levels = {fighter: ((i % 5) + 1) for i, fighter in enumerate(fighters)}  
    return fighters, fighter_types, fighter_levels  
  
# Helper function: calculates type and level bonuses (only for health and attack)  
def calculate_stats(fighter_type, fighter_level):  
    # Base stats for all fighters - only health and attack  
    base_stats = {"health": 50, "attack": 10}  
      
    # Type-specific stat modifiers  
    type_modifiers = {  
        "Purple": {"health": 1.2, "attack": 0.9},  
        "Green":  {"health": 1.3, "attack": 0.8},  
        "Blue":   {"health": 0.9, "attack": 1.0},  
        "Red":    {"health": 0.8, "attack": 1.3},  
        "Yellow": {"health": 1.0, "attack": 1.0}  
    }  
      
    # Calculate bonus based on level scaling and fighter type  
    bonus_stats = {}  
    for stat, base in base_stats.items():  
        level_multiplier = 1 + 0.05 * (fighter_level - 1)  
        type_bonus = type_modifiers.get(fighter_type, {"health": 1.0, "attack": 1.0})[stat]  
        bonus_stats[stat] = base * level_multiplier * type_bonus  
    return bonus_stats  
  
def auto_distribute_points(fighters, total_points, health_ratios):    
 
    distributed_points = {}  
    for fighter in fighters:  
        ratio = health_ratios.get(fighter, 0.5)  # default ratio if missing is 0.5  
        # Calculate initial allocation  
        health_points = round(total_points * ratio)  
        attack_points = total_points - health_points  
        # Adjust if rounding causes discrepancies (here it's already handled by subtraction)  
        distributed_points[fighter] = {"health": health_points, "attack": attack_points}  
    return distributed_points  
  
# Non-trivial function 2: Apply type and level bonuses to the distributed points.  
def apply_stat_bonuses(distributed_points, fighter_types, fighter_levels):  
 
    final_stats = {}  
    for fighter, points in distributed_points.items():  
        ftype = fighter_types.get(fighter, "Yellow")  
        flevel = fighter_levels.get(fighter, 1)  
        bonus = calculate_stats(ftype, flevel)  
        final_stats[fighter] = {  
            "health": points["health"] + bonus["health"],  
            "attack": points["attack"] + bonus["attack"]  
        }  
    return final_stats  
  
  
if __name__ == "__main__":  
    # Initialize fighters, types, and levels from our simulated paste.txt  
    fighters, fighter_types, fighter_levels = initialize_fighters()  
      
    total_bonus_points = 10  # total bonus points to distribute to each fighter  
      
    # Define desired health ratio for each fighter  
    # Here, we simulate different desired ratios for demonstration:  
    health_ratios = {fighter: 0.6 if (i % 2 == 0) else 0.4 for i, fighter in enumerate(fighters)}  
      
    print("Auto-distributing bonus points for 10 fighters:")  
    distributed_points = auto_distribute_points(fighters, total_bonus_points, health_ratios)  
    for fighter in fighters:  
        print(fighter + " -> Health bonus: " + str(distributed_points[fighter]['health']) +  
              ", Attack bonus: " + str(distributed_points[fighter]['attack']))  
      
    # Combine the distributed points with type/level bonuses  
    final_stats = apply_stat_bonuses(distributed_points, fighter_types, fighter_levels)  
      
    print("\nFinal stats after applying type and level bonuses:")  
    for fighter in fighters:  
        print(fighter + " -> Health: " + str(final_stats[fighter]['health']) +  
              ", Attack: " + str(final_stats[fighter]['attack']))  
    stats["type"] = fighter_type
    
    return stats
