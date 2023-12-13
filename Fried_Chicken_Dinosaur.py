#Author: William Taylor      
#Student ID: W0496930      
#Course: PROG1700
#Date: 10/20/23
#Project: PROG1700_<W0496930>_Fried_Chicken_Dinosaur.py
#Repository:https://github.com/W0496930/PROG1700-Algorithms
#PROG1700-Algorithms
#Programming language: Python 3
#License: Creative Commons
#Version: 1.0 of VSCode

#Program Controls
chickens_in_box = 20
daily_consumption = 1.0  
#Establish a for loop with a range of 1 to 100
for days_counter in range(1, 100):
    #The dinosaur eats one chicken on day one
    if days_counter == 1:
        daily_consumption = 1.0 
    #On the 7th day, the dinosaur feels sick and cant eat, so I incriment the daily consumption to zero.
    elif days_counter == 7:
        daily_consumption = 0.0
        print("The Dinosaur Couldn't eat anymore due to feeling ill.") 
    #Increment the daily consumption again to multiply the chicken eaten daily variable by 5 percent each day, and round it to two decimal points.
    else:
        daily_consumption = 1.0
        daily_consumption = round(daily_consumption * 1.05, 2)
    #If there is less chicken in the box then the daily consumption the dinosaur consumes all the chicken
    #As a way to make sure the program does not try to consume more chicken then there is chicken in the box.
    if chickens_in_box < daily_consumption:
        daily_consumption = chickens_in_box  
    #Increment the chickens in box counter to subtract the amount of chicken the dinosaur ate per day.
    chickens_in_box -= daily_consumption 
    #Output how much fried chicken was eaten on each day, and how much is left in the box
    print(f"Fried chicken eaten on day {days_counter} = {daily_consumption:.2f} Fried chicken remaining: {chickens_in_box:.2f}")
    #If there is no chicken left in the box, end the program.
    if chickens_in_box <= 0:
        break  
#Output how many days it took to run out of fried chicken.
print(f"Days it took to run out of fried chicken: {days_counter}")
