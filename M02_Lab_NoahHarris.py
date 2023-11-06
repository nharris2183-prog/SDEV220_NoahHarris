##############################################
# Name: Noah Harris
# File: M02_Lab_NoahHarris.py
# Date: 11/5/2023
# Description: This program will ask the user for their last name, 
# first name, and GPA. It will then tell them if they made the Dean's List,
# Honor Roll, or neither.
##############################################

# Ask user for last name or 'ZZZ' to quit
last_name = input("Enter Last Name (Enter 'ZZZ' to quit): ")

# Test if user wants to quit
if last_name == "ZZZ":
    print("End of Program")
    exit()

# Ask user for first name and GPA
first_name = input("Enter First Name: ")
gpa = float(input("Enter GPA: "))

# Test if user made the Dean's List, Honor Roll, or neither
if gpa >= 3.5:
    print("Congratulations", first_name, "you made the Dean's List!")
elif gpa >= 3.25:
    print("Congratulations", first_name, "you made the Honor Roll!")
else:
    print("Sorry", first_name, "you did not make the Honor Roll.")