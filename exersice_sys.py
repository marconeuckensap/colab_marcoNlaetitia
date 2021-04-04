#!/usr/bin/python3

# @ Add necessary import statements.
import sys
import random

secret = random.randint(1, 10) # from the module 'random'
guessed = set()

def guess_number():
    num = input # @ replace None, you need to ask the user

    try: # You can ignore this for now, we'll come back to it.
        num = int(input("\n what number are you guessing? "))
    except ValueError:
        return
    if num == secret:
        print('You did it!!! \ntimes of guesses:', len(guessed) + 1, 'times!')
        sys.exit(0)
        # @ end script with success
    elif num < 1:
        sys.exit('you guessed to low! ')
        # @ end script with error message (and remove placeholder 'pass')
    elif num > 10:
        sys.exit('you guessed to high! ')
        # @ end script with error message (and remove placeholder 'pass')
    elif num in guessed:
        print('you already guessed number', num, "before! stop using the same numbers!!!", file=sys.stderr)
        # @ print error message, don't end script
    else:
        guessed.add(num)

print('Guess a number from 1 to 10')
while True:
    guess_number()