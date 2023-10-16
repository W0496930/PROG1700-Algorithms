#Author: William Taylor      
#Student ID: W0496930      
#Course: PROG1700
#Date: 10/16/23
#Project: PROG1700_<W0496930>_Guessing_Game.py
#Repository:https://github.com/W0496930/PROG1700-Algorithms
#PROG1700-Algorithms
#Programming language: Python 3
#License: Creative Commons
#Version: 1.0 of VSCode

#Import modules here
import random

#Program control and Variables
def play_game():
    num = random.randint(1, 10)
    #Ask for the users name
    user_name = input("What's your name? ")
    guesses_allowed = 5
    invalid_input_count = 0

    #Let user know the rules
    print(f"Hi {user_name}, you have 5 attempts to guess the number I'm thinking of. Good luck!")

    #Create the attempt counter variable
    attempts_used = guesses_allowed

    #Establish the for loop
    for i in range(guesses_allowed):
        
        #Subtract one number from three after each attempt the user inputs
        attempts_used -= 1

        #Check to see if the user has input a valid input, break if the user entered a valid input
        while True:
            try:
                #Ask the user to input a valid number between one and 10
                guess = int(input("Please guess a number between 1 and 10: "))
                break  
            except ValueError:
                invalid_input_count += 1
                print("Please enter a valid number between 1 and 10.")
                
                #If the user has input an invalid input 5 times, stop the program
                if invalid_input_count >= 5:
                    print("You've entered an invalid input too many times. Goodbye.")
                    return False

        #Give the user hints if the number they input was higher or lower than the computer's number, and display how many attempts they have left
        if guess < num:
            print(f"Your guess was too low, please try again. You have {attempts_used} attempts left.")
        elif guess > num:
            print(f"Your guess was too high, please try again. You have {attempts_used} attempts left.")
        
        #Print a congratulation message if the user has guessed correctly, and tell them how many attempts it took them.
        else:
            print(f"Congratulations {user_name}! You guessed the number {num} correctly in {guesses_allowed - attempts_used} attempts!")
            return True

    #Let the user know they have run out of guesses and lost
    print(f"Sorry {user_name}, you've run out of guesses. The correct number was {num}. You used all {guesses_allowed} attempts.")
    return False

#Created a while loop to implement a play again feature, if the user inputs "yes" the program will start again, and if they input "no" then it will print a "thanks for playing message" and stop the program
while True:
    if play_game():
        play_again = input("Play Again? (Yes/No): ").lower()
    else:
        play_again = input("Play Again? (Yes/No): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
