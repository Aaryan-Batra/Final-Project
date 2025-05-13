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
    User input and validation for selecting 5 fighters
    """
    options = fighter_options()
    selected = []
    selection = False
    
    while not selection:
        print("\n Enter 5 numbers between 1-10, and make sure to put a space between each:")
        user_input = input("> ")
        choices = user_input.split()        

        if len(choices) != 5:
            print(f" Please select exactly 5 options. You chose {len(choices)}.")
            continue
        
        valid_numbers = True
        numbers = []
        for choice in choices:
            if not choice.isdigit():
                valid_numbers = False
                break
            numbers.append(int(choice))
        
        if not valid_numbers:
            print("Please enter ONLY numbers.")
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
  
import random

fighters = ["Fighter" + str(i) for i in range(1, 11)]
types = ["Red", "Blue", "Green", "Purple", "Yellow"]
type_map = {}
levels = {}

for i in range(len(fighters)):
    type_map[fighters[i]] = types[i % 5]
    levels[fighters[i]] = random.randint(1, 5)

# Set base stats and bonus
bonus_points = 10
ratios = {}

for i, f in enumerate(fighters):
    if i % 2 == 0:
        ratios[f] = 0.6
    else:
        ratios[f] = 0.4

# Distribute bonuses and apply level/type effect
final_stats = {}

for f in fighters:
    health = round(bonus_points * ratios[f])
    attack = bonus_points - health

    if type_map[f] == "Red":
        attack = attack * 1.3
        health = health * 0.8
    elif type_map[f] == "Blue":
        attack = attack * 1.0
        health = health * 0.9
    elif type_map[f] == "Green":
        attack = attack * 0.8
        health = health * 1.3
    elif type_map[f] == "Purple":
        attack = attack * 0.9
        health = health * 1.2
    else:
        attack = attack * 1.0
        health = health * 1.0

    level = levels[f]
    level_mod = 1 + 0.05 * (level - 1)
    final_stats[f] = {
        "health": 50 * level_mod + health,
        "attack": 10 * level_mod + attack
    }

print("Fighter Stats:")
for f in fighters:
print(f + ": Health = " + str(round(final_stats[f]["health"], 2)) + ", Attack = " + str(round(final_stats[f]["attack"], 2)))
