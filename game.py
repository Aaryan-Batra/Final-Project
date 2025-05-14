import random


def initialize_fighters():
    fighters = ["Fighter" + str(i) for i in range(1, 11)]
    types = ["Red", "Blue", "Green", "Purple", "Yellow"]
    type_map = {}
    levels = {}
    ratios = {}

    for i, f in enumerate(fighters):
        type_map[f] = types[i % len(types)]
        levels[f] = random.randint(1, 5)
        ratios[f] = 0.6 if i % 2 == 0 else 0.4

    return fighters, type_map, levels, ratios

def calculate_final_stats(fighters, type_map, levels, ratios, bonus_points=10):
    final_stats = {}

    for f in fighters:
        health = round(bonus_points * ratios[f])
        attack = bonus_points - health

        if type_map[f] == "Red":
            attack *= 1.3
            health *= 0.8
        elif type_map[f] == "Blue":
            attack *= 1.0
            health *= 0.9
        elif type_map[f] == "Green":
            attack *= 0.8
            health *= 1.3
        elif type_map[f] == "Purple":
            attack *= 0.9
            health *= 1.2
        else:
            attack *= 1.0
            health *= 1.0

        level = levels[f]
        level_mod = 1 + 0.05 * (level - 1)

        final_stats[f] = {
            "health": 50 * level_mod + health,
            "attack": 10 * level_mod + attack
        }

    return final_stats


def fighter_options():
    options = ["Fighter 1 (Green)", "Fighter 2 (Green)", "Fighter 3 (Blue)", "Fighter 4 (Blue)", "Fighter 5 (Red)", 
               "Fighter 6 (Red)", "Fighter 7 (Purple)", "Fighter 8 (Purple)", "Fighter 9 (Yellow)", "Fighter 10 (Yellow)"]
    
    print("\nPick any 5 fighters:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    return options

def select_options():
    """
    The user gets to pick their team
    """
    options = fighter_options()
    selected = []
    selection = False
    
    while not selection:
        print("\n Type 5 numbers between 1-10 and make sure to include a space between each (like '1 3 5 7 9'):")
        user_input = input("> ")
        choices = user_input.split()
        
        if len(choices) != 5:
            print(f"You need to pick ONLY 5 fighters!")
            continue
        
        valid_numbers = True
        numbers = []
        for choice in choices:
            if not choice.isdigit():
                valid_numbers = False
                break
            numbers.append(int(choice))
        
        if not valid_numbers:
            print("Try again.")
            continue
        
        if any(num < 1 or num > 10 for num in numbers):
            print("Make sure the numbers you ONLY pick numbers between 1 and 10")
            continue
        
        if len(set(numbers)) != 5:
            print("You can't select the same number twice! Try Again!")
            continue
        
        selected = [options[num-1] for num in numbers]
        selection = True
    
    print("\nGreat Selections:")
    for option in selected:
        print(f"- {option}")
    
    return selected


def distribute_experience(total_xp, damage_tracker):
    """
    Distributes total XP across the fighters based on the damage they dealt.

    Parameters:
    total_xp (int): Total experience points to distribute.
    damage_tracker (dict): Dictionary mapping fighter names to damage dealt.

    Returns:
    dict: Mapping of fighter names to XP awarded.
    """
    total_damage = sum(damage_tracker.values())
    if total_damage == 0:
        return {fighter: 0 for fighter in damage_tracker}

    xp_distribution = {}
    for fighter, damage in damage_tracker.items():
        xp_distribution[fighter] = round((damage / total_damage) * total_xp)
    return xp_distribution

def run_game(team, enemy_health=100, team_health=100):
    print("\n--- Battle Start! ---")
    damage_tracker = {monster: 0 for monster in team}

    round_number = 1
    while enemy_health > 0 and team_health > 0:
        print(f"\n--- Round {round_number} ---")
        for monster in team:
            if enemy_health <= 0:
                break
            damage = random.randint(5, 20)
            print(f"{monster} attacks the enemy for {damage} damage!")
            enemy_health -= damage
            damage_tracker[monster] += damage

            retaliation = random.randint(3, 10)
            print(f"Enemy hits back for {retaliation} damage!")
            team_health -= retaliation

            print(f"Enemy Health: {max(enemy_health, 0)}")
            print(f"Team Health: {max(team_health, 0)}")

            if team_health <= 0:
                break
        
        round_number += 1

    if enemy_health <= 0:
        print("\nYou won the battle!")
        total_xp = 100
        xp_distribution = distribute_experience(total_xp, damage_tracker)
        print("XP Distribution:")
        for monster, xp in xp_distribution.items():
            print(f"{monster}: {xp} XP")
    else:
        print("\nYou lost the battle!")

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
    victim_types = ["Purple", "Green", "Blue", "Red", "Yellow"]

    # The basic type of interaction that happens in the game.
    interactions = {attacker_types: victim_types}

    super_effective = [{"Purple":"Green"}, {"Green":"Blue"}, {"Blue":"Red"}, {"Red":"Yellow"}, {"Yellow":"Purple"}]
    ineffective = [{"Green": "Purple"}, {"Purple": "Yellow"}, {"Yellow": "Red"}, {"Red": "Blue"}, {"Blue": "Green"}]

    for attack in super_effective:
        if super_effective is True:
            (attack_value * 1.3)
        elif ineffective is True:
            (attack_value * 0.7)
        else:
            (attack_value * 1)
    return type_interactions


if __name__ == "__main__":
    print("Time to build your fighter squad!")
    selected_display_names = select_options()
    print("You are now ready for battle!! Good Luck!")

    # Initialize all 10 fighters
    fighters, type_map, levels, ratios = initialize_fighters()
    final_stats = calculate_final_stats(fighters, type_map, levels, ratios)

    # Print stats for all fighters
    print("\nFighter Stats:")
    for f in fighters:
        print(f + ": Health = " + str(round(final_stats[f]["health"], 2)) + ", Attack = " + str(round(final_stats[f]["attack"], 2)))

    selected_team = [f"Fighter{display.split()[1]}" for display in selected_display_names]

    # Run the battle with the selected team
    run_game(selected_team)
