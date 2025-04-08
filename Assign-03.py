#!/usr/bin/env python3

# Created By: Tony G
# Date: 2025-04-08
# Uppercase lowercase program with extra features

import constants

def main():

  # While loop
    while True:
        user_input = input("Enter a letter (or type 'exit' to quit): ")

  # Exit while loop
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

            # Checks for valid input, also a nested if statement
        if len(user_input) == 1 and user_input in constants.LETTERS_TABLE:

          # Prints respective messages for upper/lowercase
            if user_input.isupper():
                print("The letter you have inputted is uppercase.")
                print("The lowercase version is:", user_input.lower())
            elif user_input.islower():
                print("The letter you have inputted is lowercase.")
                print("The uppercase version is:", user_input.upper())

            # Check if it's in the first or second half of the alphabet
            if user_input.lower() <= 'm':
                print("This letter is in the first half of the alphabet.")
            else:
                print("This letter is in the second half of the alphabet.")
        else:
            print("Invalid input, please enter a single alphabetical letter.")

if __name__ == "__main__":
    main()
