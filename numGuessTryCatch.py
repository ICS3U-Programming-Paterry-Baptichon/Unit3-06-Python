#!/usr/bin/env python3

# Created by Paterry Baptichon junior
# Created on 2022-04-09
# This program is an updated guessing game 

import random


def main():
    # this function compares an integer to a random number
    # random number generation
    random_number = random.randint(0, 10)

    # The user's input
    user_guess = input("Enter a number between 0-10: ")
    print("")

    # the process of how the guessing game will work
    try:
        user_guess_int = int(user_guess)

        if user_guess_int == random_number:
            # output when user gets the right answer
            print("Correct! {} was the right answer."
                  .format(random_number))
        else:
            # output when the user doesnt get teh right answer
            print("Incorrect, {} was the right answer."
                  .format(random_number))
    except Exception:
        # output if the user's input ins't a number
        print("That's not a number! Try again.")
    finally:
        # thank you for playing the game output 
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()