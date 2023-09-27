 #Author: William Taylor      
 #Student ID: W0496930      
 #Course: PROG1700
 #Date: 09/27/23
 #Project: Create a simple Algorithm using the program Flowchart and pseudocode
 #Repository:https://github.com/W0496930/PROG1700-Algorithms
 #PROG1700-Algorithms
 #Programming language: Python 3
 #License: Creative Commons
 #Version: 1.0 of VSCode

#ask the user for their name, and their age in years
#establish a loop
while True:
    user_name = input("Please enter your name: ")
    age_in_years = input("Please enter your age in years: ")

    #determine if the user input a valid age
    if age_in_years.isdigit():
        age_in_years = int(age_in_years)
        
        #if they are 0 years old print a special message
        if age_in_years == 0 :
            print("You were either born today or you haven't been born yet!")
        else:
            #establish the current year
            current_year = 2023 
            
            #determine the birth year by subtracting the users age from the current year
            birth_year = current_year - age_in_years
            
            #display the users birthyear
            print(f"{user_name}, You were born in the year {birth_year}!")
        break
    #if the user did not input a valid input like a number, print this error message
    else:
        print("Error! Please input a number.")