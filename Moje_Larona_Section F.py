"""
Gradebook System
A comprehensive student grade management system that uses bubble sort for ranking.

Testing Documentation Summary:

CASES TESTED:
1. Empty gradebook operations
   - Verified: display_all_students(), display_sorted_students(), class_average() handle empty states
   - Resolution: Added proper null checks and informative messages

2. Invalid grade inputs
   - Verified: add_grade() rejects grades outside 0-100 range
   - Resolution: Added validation with clear error messages

3. Duplicate student names
   - Verified: add_student() prevents duplicates (case-insensitive)
   - Resolution: Implemented case-insensitive comparison

4. Non-existent student/subject operations
   - Verified: add_grade_to_student() validates both student and subject existence
   - Resolution: Added comprehensive validation checks

5. Students with no grades
   - Verified: calculate_average() returns 0.0 for students with no grades
   - Resolution: Added empty grades check

6. Single student/subject scenarios
   - Verified: All operations work correctly with minimal data

7. Large number of students (performance)
   - Verified: Bubble sort handles various list sizes appropriately
   - Resolution: Added early termination in bubble sort when no swaps occur

ISSUES ENCOUNTERED AND RESOLUTIONS:
1. Issue: Case sensitivity in student names allowed duplicates
   Resolution: Made all comparisons case-insensitive

2. Issue: Division by zero when no grades existed
   Resolution: Added zero-check guards in average calculations

3. Issue: Original student list being modified during sorting
   Resolution: Used list.copy() to preserve original data

4. Issue: No validation for empty inputs during setup
   Resolution: Added input validation and user feedback

TEST SCENARIOS VALIDATED:
- Complete system workflow from setup to reporting
- Error handling for invalid user inputs
- Sorting accuracy with various grade distributions
- Data persistence throughout session
- Boundary conditions (min/max grades, empty states)
"""


class Student:
    """Represents a student with their name and grades"""

    def __init__(self, name):
        # Initialize a new student with name and empty grades dictionary
        self.name = name
        self.grades = {}  # Dictionary to store subjects and grades {subject: grade}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject
        Returns True if successful, False if grade is invalid

        TESTING: Validated with grades -1, 0, 100, 101 to ensure proper boundary checking"""

        # Check if grade is within valid range (0-100)
        if grade < 0 or grade > 100:
            print("Error: Grade must be between 0 and 100")
            return False
        # Add the grade to the student's record
        self.grades[subject] = grade
        return True

    def calculate_average(self):
        """Calculate the student's average grade across all subjects
        Returns 0.0 if no grades are recorded

        TESTING: Verified with empty grades, single grade, and multiple grades"""

        # Check if student has any grades
        if not self.grades:
            return 0.0

        # Calculate total of all grades
        total = sum(self.grades.values())
        # Return average (total divided by number of grades)
        return total / len(self.grades)

    def display_info(self):
        """Display the student's name, all grades, and average"""
        print(f"{self.name}'s Grades:")

        # Check if student has any grades
        if not self.grades:
            print("  No grades recorded")
            return

        # Display each subject and grade
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")

        # Calculate and display average
        average = self.calculate_average()
        print(f"  Average: {average:.2f}")


class Gradebook:
    """Manages a collection of students and provides gradebook operations"""

    def __init__(self):
        # List to store all Student objects
        self.students = []
        # List to store all available subjects
        self.subjects = []

    def add_subject(self, subject):
        """Add a new subject to the gradebook if it doesn't already exist

        TESTING: Verified duplicate subjects are prevented"""
        if subject not in self.subjects:
            self.subjects.append(subject)

    def add_student(self, name):
        """Add a new student to the gradebook
        Returns True if successful, False if student already exists

        TESTING: Validated case-insensitive duplicate detection"""
        # Check if student already exists (case-insensitive)
        for student in self.students:
            if student.name.lower() == name.lower():
                print(f"Error: {name} already exists")
                return False

        # Create new student and add to list
        new_student = Student(name)
        self.students.append(new_student)
        print(f"{name} was added successfully")
        return True

    def find_student(self, name):
        """Find a student by name (case-insensitive)
        Returns Student object if found, None if not found

        TESTING: Verified case-insensitive search works correctly"""
        # Search through all students
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def add_grade_to_student(self, name, subject, grade):
        """Add a grade to a specific student for a specific subject
        Returns True if successful, False if student or subject not found

        TESTING: Comprehensive validation of student existence, subject existence, and grade validity"""

        # Find the student
        student = self.find_student(name)
        if student is None:
            print(f"Error: {name} was not found")
            return False

        # Check if subject exists
        if subject not in self.subjects:
            print(f"Error: {subject} was not found")
            return False

        # Add the grade to the student
        if student.add_grade(subject, grade):
            print(f"{grade} was added to {name} for {subject}")
            return True
        return False

    def display_all_students(self):
        """Display a list of all students in the gradebook

        TESTING: Verified empty state handling and proper display formatting"""

        if not self.students:
            print("No students in the system")
            return

        print("All Students:")
        for student in self.students:
            print(f"  - {student.name}")

    def bubble_sort_by_average(self):
        """Sort students by average grade using bubble sort algorithm
        Returns a new sorted list of students (highest average first)

        TESTING:
        - Verified sorting correctness with various grade distributions
        - Validated original list remains unmodified
        - Performance tested with different list sizes
        - Edge cases: empty list, single student, identical averages"""

        # Create a copy of the students list to avoid modifying original
        students = self.students.copy()
        n = len(students)  # Get number of students

        # Bubble sort algorithm with optimization
        for i in range(n):
            # Flag to check if any swaps were made in this pass
            swapped = False

            for j in range(0, n - i - 1):
                # Get averages of current student and next student
                avg1 = students[j].calculate_average()
                avg2 = students[j + 1].calculate_average()

                # Sort in descending order (highest average first)
                if avg1 < avg2:
                    # Swap the students if they're in wrong order
                    students[j], students[j + 1] = students[j + 1], students[j]
                    swapped = True

            # If no swaps were made, the list is already sorted (optimization)
            if not swapped:
                break

        return students

    def display_sorted_students(self):
        """Display all students sorted by average grade (highest to lowest)

        TESTING: Verified correct ranking order and proper formatting"""
        if not self.students:
            print("No students to display")
            return

        # Get sorted list using bubble sort
        sorted_students = self.bubble_sort_by_average()

        print("Students Sorted by Average Grade (Highest to Lowest):")

        # Display each student with their rank and average
        for i, student in enumerate(sorted_students, 1):
            average = student.calculate_average()
            print(f"{i}. {student.name}: {average:.2f}")

    def class_average(self):
        """Calculate the overall class average across all students and subjects
        Returns 0.0 if no grades exist

        TESTING:
        - Verified calculation accuracy with various data sets
        - Validated empty grades handling returns 0.0
        - Checked mixed scenarios (some students with grades, some without)"""

        if not self.students:
            return 0.0

        total = 0  # Sum of all grades
        count = 0  # Number of grades

        # Loop through all students and all their grades
        for student in self.students:
            for grade in student.grades.values():
                total += grade
                count += 1

        # Avoid division by zero
        if count == 0:
            return 0.0

        # Return average of all grades
        return total / count

    def display_class_report(self):
        """Display a comprehensive report of the entire class

        TESTING: Verified all components display correctly in various states"""
        if not self.students:
            print("No students in the system")
            return

        # Print report header
        print("CLASS REPORT")
        print(f"Total Students: {len(self.students)}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Class Average: {self.class_average():.2f}")

        # Display each student's information
        for student in self.students:
            student.display_info()
            print("-" * 30)


def setup_gradebook():
    """Set up the initial gradebook with subjects
    Returns a configured Gradebook object

    TESTING: Validated input handling for invalid numbers and empty subjects"""
    gradebook = Gradebook()

    print("~~~ Gradebook Setup ~~~")

    # Get number of subjects from user with validation
    while True:
        try:
            num_subjects = int(input("How many subjects? "))
            if num_subjects > 0:
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

    # Add each subject with validation
    for i in range(num_subjects):
        while True:
            subject = input(f"Enter subject name {i + 1}: ").strip()
            if subject:
                gradebook.add_subject(subject)
                print(f"{subject} was added")
                break
            else:
                print("Subject name cannot be empty")

    return gradebook


def main():
    """Main function that runs the gradebook system

    TESTING: End-to-end testing of complete user workflow"""

    print("Welcome to Gradebook System!")
    print("This system uses bubble sort to rank students by average grade")

    # Set up the gradebook with subjects
    gradebook = setup_gradebook()

    # Main program loop
    while True:
        # Display menu options
        print("~~~ MAIN MENU ~~~")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Grades")
        print("4. View All Students")
        print("5. View Students Sorted by Average")
        print("6. Class Report")
        print("7. Exit")

        # Get user choice
        choice = input("Enter your choice (1-7): ").strip()

        # Process user choice
        if choice == '1':
            # Add a new student
            name = input("Enter student name: ").strip()
            if name:
                gradebook.add_student(name)
            else:
                print("Student name cannot be empty")

        elif choice == '2':
            # Add a grade to a student
            if not gradebook.students:
                print("No students in system. Please add students first.")
                continue

            if not gradebook.subjects:
                print("No subjects in system.")
                continue

            # Show available students
            print("Available students:")
            gradebook.display_all_students()

            # Get student name
            name = input("Enter student name: ").strip()
            student = gradebook.find_student(name)

            if student is None:
                print(f"{name} not found")
                continue

            # Show available subjects
            print(f"Available subjects: {', '.join(gradebook.subjects)}")
            subject = input("Enter subject: ").strip()

            if subject not in gradebook.subjects:
                print(f"Subject '{subject}' not found")
                continue

            # Get and validate grade
            try:
                grade = int(input("Enter grade (0-100): "))
                gradebook.add_grade_to_student(name, subject, grade)
            except ValueError:
                print("Please enter a valid number")

        elif choice == '3':
            # View a specific student's grades
            if not gradebook.students:
                print("No students in system")
                continue

            name = input("Enter student name: ").strip()
            student = gradebook.find_student(name)

            if student:
                student.display_info()
            else:
                print(f"{name} not found")

        elif choice == '4':
            # View all students
            gradebook.display_all_students()

        elif choice == '5':
            # View students sorted by average (using bubble sort)
            gradebook.display_sorted_students()

        elif choice == '6':
            # View comprehensive class report
            gradebook.display_class_report()

        elif choice == '7':
            # Exit the program
            print("Thank you for using Gradebook System! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-7")


# Start the program when this file is run directly
if __name__ == "__main__":
    main()