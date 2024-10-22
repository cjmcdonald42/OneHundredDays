'''
Day 22: Libraries and Modules
'''

import random

def guessTheNumber(number):
    isGuessing = True
    while isGuessing is True:
        guess = int(input(f"Guess a number between 1 and {number}: "))
        if guess == number:
            print("Correct! You Win!!!")
            isGuessing = False
        elif guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
    return


isPlaying = True
while isPlaying is True:
    # print(number)  # Totally cheating...

    # Choose a range
    topNumber = int(input("Enter the top number: "))
    number = random.randint(1, topNumber)
    guessTheNumber(number)

    # Repeat the game
    again = input("Would you like to play again? (y/n): ")
    if again == "n":
        isPlaying = False
