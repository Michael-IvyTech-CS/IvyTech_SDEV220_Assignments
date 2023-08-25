"""
Name: student_qualifier
Author: Michael Barthauer
Date: 8/25/2023
Description:
Accepts a student last name, first name, and gpa as input.  Returns whether
the student specified made either the Dean's List, the Honor Roll, or both.
Repeats until the last name 'ZZZ' is entered.
"""
while True:
    last_name = str(input("Please enter the student's last name (or 'ZZZ' to quit): "))
    # str() is added to prevent the user from having to push the enter key twice

    # exit if name is ZZZ
    if last_name == 'ZZZ':
        print("Exiting program...")
        break
    first_name = input("Please enter the student's first name: ")
    gpa = float(input("Please enter the student's GPA: "))

    # compare gpa to determine Dean's List/Honor Roll status
    if gpa >= 3.5:
        print(f"Congratulations {first_name} {last_name}! You made the Dean's List!")
    if gpa >= 3.25:
        print(f"Congratulations {first_name} {last_name}! You made the Honor Roll!")
