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
def select_options():
    # List of 10 options of fighters that the user can pick from
    options = ["Fighter 1 (Green)", "Fighter 2 (Green)", "Fighter 3 (Blue)", "Fighter 4 (Blue)", "Fighter 5 (Red)", 
               "Fighter 6 (Red)", "Fighter 7 (Purple)", "Fighter 8 (Purple)", "Fighter 9 (Yellow)", "Fighter 10 (Yellow)"]
    
    print("Select 5 options from the list:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    selected = []
    selection = False
    
    while not selection:
        print("\nEnter 5 numbers between 1-10, separated by spaces:")
        user_input = input("> ")
        choices = user_input.split()        
        # Makes sure that there are only 5 options selected
        if len(choices) != 5:
            print(f"Please select exactly 5 options. You entered {len(choices)}.")
            continue
        
        # Try to convert all inputs to integers
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
        # Double check to make sure the user entered numbers within the range
        if any(num < 1 or num > 10 for num in numbers):
            print("All numbers must be between 1 and 10.")
            continue
        
        # Check to see if the user selected any duplicates 
        if len(set(numbers)) != 5:
            print("Please select 5 different options (no duplicates).")
            continue
        
        # All validation passed, get the selected options
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
def distribute_experience(total_xp, damage_dict):
    """
    Distributes experience points based on damage dealt by each team member.

    Parameters:
    total_xp (int): Total experience points gained after battle.
    damage_dict (dict): {member_name: damage_dealt}

    Returns:
    dict: {member_name: xp_awarded}
    """
    total_damage = sum(damage_dict.values())

    if total_damage == 0:
        # If no damage was dealt, evenly distribute XP
        equal_share = total_xp // len(damage_dict)
        return {member: equal_share for member in damage_dict}

    xp_distribution = {}
    for member, damage in damage_dict.items():
        contribution_ratio = damage / total_damage
        xp = round(contribution_ratio * total_xp)
        xp_distribution[member] = xp

    return xp_distribution
