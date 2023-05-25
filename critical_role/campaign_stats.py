"""Campaign Stat Tracker!"""

__author__ = "Trenton Mills"


# Initialize an empty dictionary to store character statistics
campaign_stats = {}

# Function to add a new character and their statistics
def add_character_stats(character_name):
    if character_name in campaign_stats:
        return

    campaign_stats[character_name] = {
        'damage': {},
        'healing': 0,
        'damage_taken': 0,
        'times_knocked_unconscious': 0,
        'times_killed': 0,
        'kills' : 0
    }


# Function to add damage for a specific damage type
def add_damage(character_name, damage_type, amount):
    if character_name not in campaign_stats:
        print("Character does not exist!")
        return

    character_stats = campaign_stats[character_name]
    if damage_type in character_stats['damage']:
        character_stats['damage'][damage_type] += amount
    else:
        character_stats['damage'][damage_type] = amount


# Function to update healing amount
def update_healing(character_name, amount):
    if character_name not in campaign_stats:
        print("Character does not exist!")
        return

    character_stats = campaign_stats[character_name]
    character_stats['healing'] += amount


# Function to update damage taken
def update_damage_taken(character_name, amount):
    if character_name not in campaign_stats:
        print("Character does not exist!")
        return

    character_stats = campaign_stats[character_name]
    character_stats['damage_taken'] += amount


# Function to update the number of times knocked unconscious
def update_times_knocked_unconscious(character_name, count=1):
    if character_name not in campaign_stats:
        print("Character does not exist!")
        return

    character_stats = campaign_stats[character_name]
    character_stats['times_knocked_unconscious'] += count


# Function to update the number of times killed
def update_times_killed(character_name, count=1):
    if character_name not in campaign_stats:
        print("Character does not exist!")
        return

    character_stats = campaign_stats[character_name]
    character_stats['times_killed'] += count


# Increments the number of kills per player
def increment_kills(character_name):
    if character_name not in campaign_stats:
        print("Character does not exist!")
        return

    character_stats = campaign_stats[character_name]
    character_stats['kills'] += 1


# Accessing character statistics
def get_character_stats(character_name):
    if character_name not in campaign_stats:
        print("Character does not exist!")
        return

    character_stats = campaign_stats[character_name]
    print("Character:", character_name)
    print("Damage:")
    for damage_type, amount in character_stats['damage'].items():
        print(f"{damage_type}: {amount}")
    print("Healing:", character_stats['healing'])
    print("Damage Taken:", character_stats['damage_taken'])
    print("Times Knocked Unconscious:", character_stats['times_knocked_unconscious'])
    print("Times Killed:", character_stats['times_killed'])
    print("Amount of kills:", character_stats['kills'])
    print("---------------")


# Combines all the statistics
def get_combined_stats():
    combined_stats = {
        'damage_types': {},
        'healing_amount': 0,
        'damage_taken': 0,
        'times_unconscious': 0,
        'times_killed': 0,
        'kills': 0
    }

    for character_stats in campaign_stats.values():
        for damage_type, amount in character_stats['damage_type'].items():
            if damage_type not in combined_stats['damage_type']:
                combined_stats['damage_type'][damage_type] = 0
            combined_stats['damage_type'][damage_type] += amount

        combined_stats['healing_amount'] += character_stats['healing_amount']
        combined_stats['damage_taken'] += character_stats['damage_taken']
        combined_stats['times_unconscious'] += character_stats['times_unconscious']
        combined_stats['times_killed'] += character_stats['times_killed']

    print("Combined Stats:")
    print("Damage Types:")
    for damage_type, amount in combined_stats['damage_types'].items():
        print(f"- {damage_type}: {amount}")
    print("Healing Amount:", combined_stats['healing_amount'])
    print("Damage Taken:", combined_stats['damage_taken'])
    print("Times Unconscious:", combined_stats['times_unconscious'])
    print("Times Killed:", combined_stats['times_killed'])


enemy_stats = {}

# Tracks enemy damage
def add_enemy_damage(enemy_name, damage_type, damage_amount):
    if enemy_name not in enemy_stats:
        enemy_stats[enemy_name] = {}

    if damage_type not in enemy_stats[enemy_name]:
        enemy_stats[enemy_name][damage_type] = 0

    enemy_stats[enemy_name][damage_type] += damage_amount


# Accesses the enemies damage stats
def get_enemy_stats(enemy_name):
    if enemy_name not in enemy_stats:
        print("Enemy does not exist!")
        return

    enemy_damage_stats = enemy_stats[enemy_name]

    print(f"Damage statistics for {enemy_name} is:")
    for damage_type, damage_amount in enemy_damage_stats.items():
        print(f"{damage_type}: {damage_amount}")


# Combines all the enemy damage done
def get_total_enemy_damage():
    total_damage = 0
    for enemy_damage_stats in enemy_stats.values():
        for damage_amount in enemy_damage_stats.values():
            total_damage += damage_amount
    return total_damage