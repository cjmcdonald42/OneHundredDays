'''
Day 18
Guess a random number between 1 and 100
'''

import random

# Pick a random number
number = random.randint(1, 100)


isPlaying = True
while isPlaying is True:
    # print(number)  # Totally cheating...
    isGuessing = True
    while isGuessing is True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print("Correct! You Win!!!")
            isGuessing = False
        elif guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")

    # Repeat the game
    again = input("Would you like to play again? (y/n): ")
    if again == "n":
        isPlaying = False
