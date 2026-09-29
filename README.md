Student Grade Calculator
A simple console application in Python for adding students with marks of five subjects, calculating
percentage and grade automatically, and searching results by roll number.
Features
• Add a student with name, roll number and marks of 5 subjects
• Automatic percentage (average of 5 marks) and grade calculation
• Grades: A+ (90 and above), A (80), B (70), C (60), D (50), F (below 50)
• Display all stored student records
• Search a student by roll number
• Show a short result card for a roll number
• Messages for no records, student not found and invalid menu choice
Requirements
• Python 3.6 or higher
• No external libraries needed
How to Run
• 1. Extract the zip and open a terminal in the folder.
• 2. Run: python student_grade_calculator.py
• 3. Follow the on-screen menu.
Menu Options
Option Action
1 Add Student
2 Display All Students
3 Search Student
4 Show Result
5 Exit
Grade Slabs
Percentage Grade
90 or more A+
80 to below 90 A
70 to below 80 B
60 to below 70 C
50 to below 60 D
Below 50 F
Page | 1
Student Grade Calculator – README
 Sample Usage
Enter your choice: 1
Enter student name: Aman Raj
Enter roll number: 101
Enter marks of 5 subjects:
Subject 1: 95
Subject 2: 92
Subject 3: 88
Subject 4: 90
Subject 5: 95
Student added successfully!
Enter your choice: 4
Enter roll number: 101
========== RESULT ==========
Name : Aman Raj
Roll No : 101
Percentage : 92.0 %
Grade : A+
============================
Notes
• Data is stored in memory and is not saved after exit.
• Marks are assumed to be out of 100 for each subject.
• Entering non-numeric text for marks will raise an error (see Report for suggested improvements).
• Marks are not range-checked, so negative marks or marks above 100 are accepted.
• Duplicate roll numbers are allowed; search shows the first match. Roll number search is exact and
case-sensitive.
Files
• 1_Statement.pdf - problem statement
• 2_ReadMe.pdf - this file
• 3_Report.pdf - project report
• 4_Code.pdf - source code listing
• student_grade_calculator.py - runnable source file
