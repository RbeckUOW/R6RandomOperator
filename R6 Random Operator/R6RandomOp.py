import random


def get_random_name(role):
    # Operator names
    attackers = ["Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz",
                 "Fuze", "Blitz", "IQ", "Buck", "Blackbeard", "Capitao", "Hibana", "Jackal",
                 "Ying", "Zofia", "Dokkaebi", "Lion", "Finka", "Maverick", "Nomad", "Gridlock",
                 "Nokk", "Amaru", "Kali", "Iana", "Ace", "Zero", "Flores", "Osa", "Sens", "Grim",
                 "Brava", "Ram"]
    defenders = ["Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachanka", "Jager",
                 "Bandit", "Frost", "Valkyrie", "Caviera", "Echo", "Mira", "Lesion", "Ela", "Vigil",
                 "Maestro", "Alibi", "Clash", "Kaid", "Mozzie", "Warden", "Goyo", "Wamai", "Oryx", "Melusi", "Aruni",
                 "Thunderbird", "Thorn", "Azami", "Solis", "Fenrir"]

    if role.lower() == 'attacker':
        return random.choice(attackers)
    elif role.lower() == 'defender':
        return random.choice(defenders)
    else:
        return "Invalid role. Please choose 'attacker' or 'defender'."


while True:

    # Specifying which team the user is on
    user_input = input("Enter 'attacker' or 'defender' or 'exit' to end: ")

    # Loop until exit
    if user_input.lower() == 'exit':
        print("GGWP")
        break

    # Random operator name given from user selection
    random_name = get_random_name(user_input)
    print(f"Random {user_input} name: {random_name}")

# Developed by Ryan Beck-2024
# This work is my own, please do not redistribute without proper credit
