# Write a function that generates a random number between 1 and 100 and asks the user to guess it.
# Provide feedback to the user after each guess (e.g., "Too high!" or "Too low!").
# The game continues until the user guesses the correct number.
#
# RETURNS a boolean

import random


def guess_the_number():
    secret_number = random.randint(1, 100)
    print("Your secret number is", secret_number)
    # TODO: Implement the game logic
    guess=5
    if secret_number >guess:
        print("Too high!")
    else:
        print ( "Too low!")

    pass

# Start the game
guess_the_number()
