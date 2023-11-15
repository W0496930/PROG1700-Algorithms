#Author: William Taylor      
#Student ID: W0496930      
#Course: PROG1700
#Date: 2023-11-15
#Project: W0496930_PROG1700_Dictionary_Excercise
#Repository:https://github.com/W0496930/PROG1700-Algorithms
#PROG1700-Algorithms
#Programming language: Python 3
#License: Creative Commons
#Version: 1.0 of VSCode


#Establish every students score
student_scores = {
    "Micheal": 80,
    "Shelby": 95,
    "George": 65,
    "Bob": 45,
    "Richard": 90
}

#Determine what each students average score is, and then print it
average_score = sum(student_scores.values()) / len(student_scores)
print("Average score:", average_score)

#Ask the user search for a student
student_name = input("Search for a student: ")

#If the student isnt inside of the dictionary, print a student not found message, and if they are found, print their name and their score.
if student_name in student_scores:
    print(f"{student_name}'s score is {student_scores[student_name]}")
else:
    print(f"Student {student_name} not found.")

#Ask the user to update the score of one of the students and then print all of the students with the updated scores.
update_name = input("Enter the name of the student to update: ")
if update_name in student_scores:
    student_scores[update_name] = int(input(f"Enter {update_name}'s new score: "))
    print("Updated student scores:", student_scores)
#Print another student not found message if they arent inside of the dictionary
else:
    print(f"Student {update_name} not found.")

#Ask the user to remove a student from the dictionary
remove_name = input("Enter the name of the student to remove: ")
#If student isnt found, print another student not found message
if remove_name in student_scores:
    del student_scores[remove_name]
    print(f"Removed {remove_name} from student scores.")
else:
    print(f"Student {remove_name} not found.")

#Print the highest score out of each of the students and their name.
best_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[best_student]
print(f"The student with the highest score is {best_student} with a score of {highest_score}.")
