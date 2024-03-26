# Task 1: Random Choice Game

import random

numbers = [1, 2, 3, 4, 5]

chosen = random.choice(numbers)

guess = int(input("Guess a number from 1-5"))

if chosen == guess:
    print("The right number was" + " " + str(chosen) + ". Lucky Guess...")
else:
    print("The right number was" + " " + str(chosen) + ". Try looking at Unix time and calculating the answer!")
