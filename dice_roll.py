# Dice Roll Library, Joshua Clark, February 18, 2021, 12:26PM, v0.3

# d4 Simulator
def roll_d4(num_roll): # num_roll is an ARGUMENT.
    import random
    import time

    rolls = 0
    sum = 0
    while rolls <= num_roll:
        result = random.randint(1,4)
        print(f"You rolled a {result} on the d4!\n"
        rolls +=1
        time.sleep(1)
        sum += result
    print(f"The total roll was {sum}.\num_roll")    


    


