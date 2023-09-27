 #William Taylor      
 #W0496930      
 #2023-09-25
 #(Version 1.82 of VSCode) 

#ask the user for their name, and their age in years
#loop
while True:
    user_name = input("Please enter your name: ")
    age_in_years = input("Please enter your age in years: ")

    #determine if the user input a valid age (or if they are 0 years old)
    if age_in_years.isdigit():
        age_in_years = int(age_in_years)
        
        if age_in_years == 0 :
            print("You were either born today or you haven't been born yet!")
        else:
            #calculate the current year
            current_year = 2023 
            
            #determine the birth year
            birth_year = current_year - age_in_years
            
            #display the users birthyear
            print(f"{user_name}, You were born in the year {birth_year}!")
        break
    else:
        print("Error! Please input a number.")