class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # {subject: grade}

    def add_grade(self, subject, grade):
        """Add or update a grade for a subject"""
        self.grades[subject] = grade

    def remove_grade(self, subject):
        """Remove a grade for a specific subject"""
        if subject in self.grades:
            del self.grades[subject]
            return True
        return False

    def calculate_average(self):
        """Calculate the student's average grade"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_grade(self, subject):
        """Get grade for a specific subject"""
        return self.grades.get(subject, None)

    def display_info(self):
        """Display student's grades and average"""
        print(f"\n{self.name}'s Results:")
        if not self.grades:
            print("  No grades recorded")
            return

        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")

        average = self.calculate_average()
        print(f"  Average: {average:.2f}")

    def has_subject(self, subject):
        """Check if student has a grade for the given subject"""
        return subject in self.grades

    def __str__(self):
        return f"Student: {self.name}, Grades: {len(self.grades)}, Average: {self.calculate_average():.2f}"


class Gradebook:
    def __init__(self):
        self.students = {}  # {name: Student object}
        self.subjects = set()

    def add_subject(self, subject):
        """Add a subject to the gradebook"""
        self.subjects.add(subject)

    def subject_exists(self, subject):
        """Check if subject exists"""
        return subject in self.subjects

    def add_student(self, name):
        """Add a new student to the gradebook"""
        if name in self.students:
            return False  # Student already exists
        self.students[name] = Student(name)
        return True

    def remove_student(self, name):
        """Remove a student from the gradebook"""
        if name in self.students:
            del self.students[name]
            return True
        return False

    def get_student(self, name):
        """Get student object by name"""
        return self.students.get(name, None)

    def student_exists(self, name):
        """Check if student exists"""
        return name in self.students

    def update_student_grade(self, name, subject, grade):
        """Update or add a grade for a student"""
        if name not in self.students:
            return False
        self.students[name].add_grade(subject, grade)
        return True

    def search_student(self, name):
        """Search for a student and return their object"""
        return self.students.get(name, None)

    def get_all_students(self):
        """Get all student objects"""
        return list(self.students.values())

    def sort_students_by_average(self, descending=True):
        """Sort students by their average grade"""
        sorted_students = sorted(
            self.students.values(),
            key=lambda student: student.calculate_average(),
            reverse=descending
        )
        return sorted_students

    def sort_students_by_subject(self, subject, descending=True):
        """Sort students by grade in a specific subject"""

        def subject_grade(student):
            grade = student.get_grade(subject)
            return grade if grade is not None else -1  # Students without grade go last

        sorted_students = sorted(
            self.students.values(),
            key=subject_grade,
            reverse=descending
        )
        return sorted_students

    def subject_stats(self, subject):
        """Get statistics for a specific subject"""
        grades = []
        for student in self.students.values():
            grade = student.get_grade(subject)
            if grade is not None:
                grades.append(grade)

        if not grades:
            return None, None, 0, 0

        highest = max(grades)
        lowest = min(grades)
        average = sum(grades) / len(grades)
        return highest, lowest, average, len(grades)

    def class_average(self):
        """Calculate overall class average"""
        total_grade = 0
        total_subjects = 0

        for student in self.students.values():
            for grade in student.grades.values():
                total_grade += grade
                total_subjects += 1

        if total_subjects == 0:
            return 0
        return total_grade / total_subjects

    def class_report(self):
        """Make a class report"""
        if not self.students:
            print("No students in the system")
            return

        print("\n~~~ Class Report ~~~")
        print(f"Total Students: {len(self.students)}")
        print(f"Subjects: {', '.join(sorted(self.subjects))}")
        print(f"Overall Class Average: {self.class_average():.2f}\n")

        for student in self.students.values():
            student.display_info()

    def subject_summary(self):
        """Generate summary for all subjects"""
        if not self.subjects:
            print("No subjects defined")
            return

        print("\n~~~ Subject Summary ~~~")
        for subject in sorted(self.subjects):
            highest, lowest, average, count = self.subject_stats(subject)
            print(f"\n{subject}:")
            if highest is not None:
                print(f"  Highest Grade: {highest}")
                print(f"  Lowest Grade: {lowest}")
                print(f"  Average: {average:.2f}")
                print(f"  Students with grade: {count}")
            else:
                print(f"  No grades recorded")

    def summary_table(self):
        """Generate a summary table"""
        if not self.students:
            print("No students in the system")
            return

        print("\n~~~ Student Summary Table ~~~")

        # Header
        header = f"{'Name':<15}"
        for subject in sorted(self.subjects):
            header += f"{subject:<12}"
        header += "Average"
        print(header)
        print("-" * len(header))

        # Student rows
        for student in self.students.values():
            row = f"{student.name:<15}"
            total = 0
            valid_subjects = 0

            for subject in sorted(self.subjects):
                grade = student.get_grade(subject)
                if grade is not None:
                    row += f"{grade:<12}"
                    total += grade
                    valid_subjects += 1
                else:
                    row += f"{'N/A':<12}"

            if valid_subjects > 0:
                average = total / valid_subjects
                row += f"{average:.2f}"
            else:
                row += "N/A"
            print(row)


class GradebookManager:
    def __init__(self):
        self.gradebook = Gradebook()

    @staticmethod
    def valid_grade(prompt):
        """Get a valid grade between 0-100"""
        while True:
            try:
                grade = int(input(prompt))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("Grade must range from 0 to 100")
            except ValueError:
                print("Please enter a valid number")

    @staticmethod
    def get_student_name(prompt):
        """Get student name with validation"""
        while True:
            name = input(prompt).strip()
            if name:
                return name
            print("Student name cannot be empty")

    def setup_subjects(self):
        """Setup subjects for the gradebook"""
        while True:
            try:
                num_subjects = int(input("How many subjects does each student have? "))
                if num_subjects > 0:
                    break
                else:
                    print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")

        for i in range(num_subjects):
            while True:
                subject_name = input(f"Enter subject name {i + 1}: ").strip()
                if subject_name:
                    self.gradebook.add_subject(subject_name)
                    break
                else:
                    print("Subject name cannot be empty")

    def add_student_interactive(self):
        """Interactive method to add a new student"""
        name = self.get_student_name("Enter student's name: ")

        if not self.gradebook.add_student(name):
            print(f"{name} already exists in the system")
            return

        print(f"{name} was added successfully")

        # Add grades for each subject
        for subject in self.gradebook.subjects:
            grade = self.valid_grade(f"Enter marks for {subject}: ")
            self.gradebook.update_student_grade(name, subject, grade)

    def update_student_grade_interactive(self):
        """Interactive method to update student grade"""
        name = self.get_student_name("Enter student's name: ")

        student = self.gradebook.get_student(name)
        if not student:
            print(f"{name} was not found")
            return

        print(f"{name}'s current grades:")
        for subject in self.gradebook.subjects:
            grade = student.get_grade(subject)
            display_grade = grade if grade is not None else "No grade found"
            print(f"  {subject}: {display_grade}")

        subject = input("Enter subject to be updated: ").strip()

        if not self.gradebook.subject_exists(subject):
            print(f"{subject} was not found in the system")
            return

        if not student.has_subject(subject):
            print(f"{subject} was not found under {name}")
            add_grade = input(f"Do you want to add a grade for {subject}? (y/n): ").lower()
            if add_grade != 'y':
                return

        grade = self.valid_grade(f"Enter marks for {subject}: ")
        self.gradebook.update_student_grade(name, subject, grade)
        print(f"{subject} grade for {name} was successfully updated to {grade}")

    def remove_student_interactive(self):
        """Interactive method to remove a student"""
        name = self.get_student_name("Enter student to be removed: ")

        if self.gradebook.student_exists(name):
            confirm = input(f"Are you sure you want to remove {name}? (y/n): ").lower()
            if confirm == 'y':
                self.gradebook.remove_student(name)
                print(f"{name} was successfully removed")
            else:
                print("Removal terminated")
        else:
            print(f"{name} was not found in the system")

    def display_student_profile(self):
        """Display a student's profile"""
        name = self.get_student_name("Enter the student's name: ")
        student = self.gradebook.get_student(name)
        if student:
            student.display_info()
        else:
            print(f"{name} was not found in the system")

    def display_subject_profile(self):
        """Display grades for a specific subject"""
        subject = input("Enter the name of the subject: ").strip()

        if not self.gradebook.subject_exists(subject):
            print(f"{subject} does not exist")
            return

        print(f"{subject} Grades:")
        highest_grade, lowest_grade, average_grade, student_count = self.gradebook.subject_stats(subject)

        # Display individual student grades
        for student in self.gradebook.students.values():
            grade = student.get_grade(subject)
            if grade is not None:
                print(f"  {student.name}: {grade}")

        # Display statistics
        if highest_grade is not None:
            print(f"Subject Statistics:")
            print(f"  Highest Grade: {highest_grade}")
            print(f"  Lowest Grade: {lowest_grade}")
            print(f"  Average: {average_grade:.2f}")
            print(f"  Number of Students: {student_count}")
        else:...
        print(f"No grades recorded for {subject}")

    def search_student_interactive(self):
        """Interactive student search"""
        name = self.get_student_name("Who are you looking for?: ")
        student = self.gradebook.search_student(name)
        if student:
            print(f"{name} was found in the system")
            student.display_info()
        else:
            print(f"{name} does not exist")

    def display_sorted_students(self):
        """Display students sorted by average or subject"""
        print("Sort Students By:")
        print("1. Average Grade (Highest to Lowest)")
        print("2. Average Grade (Lowest to Highest)")
        print("3. Specific Subject Grade (Highest to Lowest)")
        print("4. Specific Subject Grade (Lowest to Highest)")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sorted_students = self.gradebook.sort_students_by_average(descending=True)
            print("Students sorted by Average (Highest to Lowest):")
        elif choice == '2':
            sorted_students = self.gradebook.sort_students_by_average(descending=False)
            print("Students sorted by Average (Lowest to Highest):")
        elif choice in ['3', '4']:
            subject = input("Enter subject name: ").strip()
            if not self.gradebook.subject_exists(subject):
                print(f"Subject '{subject}' not found")
                return
            descending = (choice == '3')
            sorted_students = self.gradebook.sort_students_by_subject(subject, descending=descending)
            order = "Highest to Lowest" if descending else "Lowest to Highest"
            print(f"Students sorted by {subject} ({order}):")
        else:
            print("Invalid choice")
            return

        for i, student in enumerate(sorted_students, 1):
            if choice in ['1', '2']:
                print(f"{i}. {student.name}: {student.calculate_average():.2f}")
            else:
                grade = student.get_grade(subject)
                grade_display = grade if grade is not None else "N/A"
                print(f"{i}. {student.name}: {grade_display}")

    @staticmethod
    def display_menu():
        """Display the main menu"""
        print("~~~ Main Menu ~~~")
        print("1. Add New Student")
        print("2. Update Student's Grade")
        print("3. Remove Current Student")
        print("4. Student Grades Profile")
        print("5. Subject Grades Profile")
        print("6. Student Search")
        print("7. Display Sorted Students")
        print("8. Class Report")
        print("9. Subject Summary")
        print("10. Summary Table")
        print("11. Class Overall Average")
        print("12. Exit")

    @staticmethod
    def get_menu_choice():
        """Get valid menu choice"""
        while True:
            try:
                choice = int(input("Enter your choice (1-12): "))
                if 1 <= choice <= 12:
                    return choice
                else:
                    print("Please enter a number between 1 and 12")
            except ValueError:
                print("Please enter a valid number")

    def run(self):
        """Main program loop"""
        print("~~~ Student GradeBook Management System ~~~")
        self.setup_subjects()

        while True:
            self.display_menu()
            option = self.get_menu_choice()

            if option == 1:
                self.add_student_interactive()
            elif option == 2:
                self.update_student_grade_interactive()
            elif option == 3:
                self.remove_student_interactive()
            elif option == 4:
                self.display_student_profile()
            elif option == 5:
                self.display_subject_profile()
            elif option == 6:
                self.search_student_interactive()
            elif option == 7:
                self.display_sorted_students()
            elif option == 8:
                self.gradebook.class_report()
            elif option == 9:
                self.gradebook.subject_summary()
            elif option == 10:
                self.gradebook.summary_table()
            elif option == 11:
                overall_avg = self.gradebook.class_average()
                print(f"Overall Class Average: {overall_avg:.2f}")
            elif option == 12:
                print("Adios")
                break


# Unit Tests
def run_tests():
    """Comprehensive unit tests for the OOP system"""
    print("Running unit tests...")

    # Test Student class
    student1 = Student("Ari Grande")
    student1.add_grade("Math", 90)
    student1.add_grade("Music", 95)

    assert student1.name == "Ari Grande"
    assert student1.get_grade("Math") == 85
    assert student1.calculate_average() == 88.5
    assert student1.has_subject("Math") == True
    assert student1.has_subject("History") == False

    # Test Gradebook class
    gradebook = Gradebook()
    gradebook.add_subject("Math")
    gradebook.add_subject("Music")

    assert gradebook.add_student("Ari Grande") == True
    assert gradebook.add_student("Ari Grande") == False  # Duplicate

    gradebook.update_student_grade("Ari Grande", "Math", 98)
    gradebook.update_student_grade("Ari Grande", "Music", 100)

    student = gradebook.get_student("Ari Grande")
    assert student is not None
    assert student.calculate_average() == 92.5

    # Test sorting
    gradebook.add_student("Dalton Gomez")
    gradebook.update_student_grade("Dalton Gomez", "Math", 65)
    gradebook.update_student_grade("Dalton Gomez", "Science", 60)

    sorted_by_avg = gradebook.sort_students_by_average()
    assert sorted_by_avg[0].name == "Ari Grande"  # Higher average

    print("All tests passed! ✓")


def main():
    """Main function to run the program"""
    # Uncomment the line below to run tests
    # run_tests()

    manager = GradebookManager()
    manager.run()


if __name__ == "__main__":
    main()