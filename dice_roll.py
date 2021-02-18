# Dice Roll Library, Joshua Clark, February 18, 2021, 12:26PM, v0.0

# d4 Simulator
def roll_d4(num_roll): # num_roll is an ARGUMENT.
    import random

    rolls = 0
    while rolls <= num_roll:
        result = random.randint(1,4)
        print(f"You rolled a {result} on the d4!\n"
        rolls +=1