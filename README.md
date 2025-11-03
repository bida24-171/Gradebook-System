Python Gradebook System Assignment
Section A: A Basic Grading System (Moje_Larona_SectionA.py)
This is where the program is introduced with a list to store the students' information like their total, names, grades, and average marks they achieved as a class.
Features:
Input student names using the variable num_student and the grades with the variable grade and an if statement, a while loop along with exception handling. 
The program also calculates the overall class average by dividing the total grades with the number of students.
Section B: A Grading System with multiple subjects (Moje_Larona_SectionB.py)
This is an improved program that asks the user for number of subjects the students do and store in a variable called num_subjects.
Features:
There are individual student averages by dividing the sum of each student's grades and the number of subjects they do .
There is information about the highest, lowest, and average grade in each subject that can be called through built in functions like max for the highest grade, minimum for the lowest grade and calculating the average with sum and length function.
There is also a summary table that shows the shows the name and their average. 
Section C: A Dictionary based Grading System (Moje_Larona_Section.py)
This is where dictionaries were introduced so that we could contain information under 2 structures instead of multiple lists. The dictionaries introduced were students and subjects.
There was in introduction of functions like adding students, upgrading there grades, removing students, a student profile, a subject’s profile, searching for a specific student, subject summary, summary table, overall average, set up for subjects and the main. 
The main is the program that is shown after asking for the number of students, number of subjects, and the name of said subjects. There is a list of choices which the user must pick from to perform a specific task.

Section D: An enhanced Dictionary System (Moje_Larona_SectionD.py)
This is the dictionary program enhanced with modularization  and improved exception handling.
Section E: Object Oriented Implementation (Moje_Larona_SectionE.py)
Here is where classes, objects and methods were introduced. There are two classes called Student and Gradebook.
Sorting the average and subject grades of students is a new feature that was added to the main menu.
There were tests that were done and documented.
Section F: Algorithm Enhancement System(Moje_Larona_SectionF.py)
This is where the bubble sort method was introduced to rank the students.
There were more tests done and documented.
Usage
To use this management system, the python used must be 3.13.7  or higher.
Running the program 
Section A and B are the basic programs.
Section C and D are the medium level programs.
Section E and F are the advanced programs.
The user needs to follow the interactive prompts to set up subjects and manage students.
The common features across the sections are adding, removing, and updating the students, grade input, and validation, calculating the student and class averages, reports, and statistics.
The advanced features are object-oriented designs, sorting algorithms, testing and advanced searching.




Main Menu
1. Adding a new student
2. Updating a student’s grade
3. Removing a current student
4. Student’s grade profile
5. Subject grade profile
6. Student Search
7. Display sorted students
8. Class Report
9. Subject Summary
10. Summary Table
11. Class Overall Average
12. Exit
Assumptions
Grade scale: All grades are assumed to be between 0-100.
All inputs and outputs should be in English.
Limitations
All data will be lost when program exits.
Bubble sorting may be inefficient. 
There is no user login to use the program.
Can not export reports.
Input Guidelines
Student Names:
Cannot be empty, cannot be numeric only	, case-insensitive, and special characters are not allowed.
Grade input:
Must be integers between 0 and 100, decimal grades are shortened, negative numbers are rejected, and non-numeric data raise an error message.
Subject names:
Cannot be empty, duplicates are prevented and case-sensitive for display.
Error Recovery
Invalid inputs: program prompts for re-entry.
System Errors: Gracefully terminates the program with error handling.
Upgrades to Consider
Advanced sorting algorithms
Data export capabilities
User authentication system





 


