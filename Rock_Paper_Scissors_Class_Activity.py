 #Author: William Taylor      
 #Student ID: W0496930      
 #Course: PROG1700
 #Date: 10/04/23
 #Project: Rock Paper Scissors Class Activity
 #Repository:https://github.com/W0496930/PROG1700-Algorithms
 #PROG1700-Algorithms
 #Programming language: Python 3
 #License: Creative Commons
 #Version: 1.0 of VSCode

#Import modules here
import random 

#Variables
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

#Program Control 
while True:
    user_action = input("Enter your choice! (Rock, Paper, Scissors)").lower()
    
    #Variables
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
   
    #Validate the input to see if the user input rock paper or scissors
    while user_action not in possible_actions:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")
        user_action = input("Enter your choice! (Rock, Paper, Scissors)").lower()

    #Determine what the user and computer chose, and then display the result
    print(f"\nYou chose {user_action}, and I chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both of us selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    #Ask the user if they want to play again using the "play_again" variable
    play_again = input("play again? (yes/no): ")   
    if play_again.lower()   != "yes":
        break   
