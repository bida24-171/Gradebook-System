"""Dictionaries"""
students = {}
subjects = {}

def valid_grade(prompt):
    """Checks if grade is valid"""
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must range from 0 to 100")
        except ValueError:
            print("Please enter a valid number")

def student_name(prompt):
    """Checks if name isn't blank and not numeric"""
    while True:
        name = input(prompt).strip()
        if name and not name.isdigit():
            return name
        print("Student name cannot be empty or numeric")

def student_presence(name):
    """checks presence of student"""
    return name in students

def subject_presence(subject):
    """checks presence of subject"""
    return subject in subjects

def student_average(grade_dict):
    """calculates a certain student's average grade"""
    if not grade_dict:
        return 0
    return sum(grade_dict.values())/len(grade_dict)

def subject_stats(grades_list):
    """calculates the stats for a subject"""
    if not grades_list:
        return 0
    highest_grade = max(grades_list)
    lowest_grade = min(grades_list)
    average_grade = sum(grades_list)/len(grades_list)
    return highest_grade, lowest_grade, average_grade

def student_grades(name):
    """displays a student's grades and average"""
    if not student_presence(name):
        print(f"{name} was not found in the system")
        return False

    print(f"{name}'s Results:")
    total = 0
    for subject, grade in students[name].items():
        print(f" {subject}: {grade}")
        total +=grade

    if students[name]:
        average = student_average(students[name])
        print(f"Average:{average:.2f}")
    else:
        print("We didn't find any grades under this student")

    return True

def add_students():
    """Adds a new student to the system"""
    name = student_name("Enter student's name: ")

    if student_presence(name):
        print(f"{name} already exists in the system")
        return

    students[name] = {}
    print(f"{name} was add successfully")

    for subject in subjects:
        grade = valid_grade(f"Enter marks for {subject}: ")
        students[name][subject] = grade

def student_grade_update():
    """Updates a specific subject for a student"""
    name = student_name("Enter student's name: ")

    if not student_presence(name):
        print(f"{name} was not found")
        return

    print(f"{name}'s current grades:")
    for subject in subjects:
        current_grade = students[name].get(subject, "No grade found")
        print(f" {subject}: {current_grade}")

    subject = input("Enter subject to be updated: ").strip()

    if not subject_presence(subject):
        print(f"{subject} was not found in the system")
        return

    if subject not in students[name]:
        print(f"{subject} was not found under {name} ")
        add_grade = input(f"Do you want to add a grade for {subject}? (y/n): ").lower()

        if add_grade != 'y':
            return

        grade = valid_grade(f"Enter marks for {subject}: ")
        students[name][subject] = grade
        print(f"{subject} grade for {name} was successfully added: {grade}")

    else:
        grade = valid_grade(f"Enter updated marks for {subject}: ")
        students[name][subject] = grade
        print(f"{subject} grade for {name} was updated successfully to {grade}")

def remove_student():
    """Removes a specific student from the Gradebook System"""
    name = student_name("Enter student to be removed: ")

    if student_presence(name):
        confirm = input(f"Are you sure you want to remove {name}? (y/n): ").lower()
        if confirm == 'y':
            del students[name]
            print(f"{name} was successfully removed")
        else:
            print("Removal terminated")
    else:
        print(f"{name} was not found in the system")

def student_profile():
    """Shows a specified student's grades"""
    name = student_name("Enter the student's name: ")
    student_grades(name)

def subject_profile():
    """Shows the grades of a specific subject"""
    subject = input("Enter the name of the subject: "). strip()

    if not subject_presence(subject):
        print(f"{subject} does not exist")
        return

    print(f"{subject} Grades:")
    subject_grades = []

    for name, grade_dict in students.items():
        if subject in grade_dict:
            grade = grade_dict[subject]
            print (f" {name}: {grade}")
            subject_grades.append(grade)

    if subject_grades:
        highest_grade, lowest_grade, average_grade = subject_stats(subject_grades)
        print(f"Subject Statistics:")
        print(f" Highest Grade: {highest_grade}")
        print(f" Lowest Grade: {lowest_grade}")
        print(f" Average: {average_grade:.2f}")
        print(f" Number of Students: {len(subject_grades)}")
    else:
        print(f"No grades recorded for {subject}")

def search_student():
    """Searches for a specific student and outputs their info"""
    name = student_name("Who are you looking for?: ")

    if student_grades(name):
        print(f"{name} was found in the system")
    else:
        print(f"{name} does not exist")

def class_report():
    """Creates a class report"""
    if not students:
        print("No students in the system")
        return

    print("~~~ Class Report~~~")
    print(f"Total Students: {len(students)}")
    print(f"Subjects: {','.join(subjects.keys())}")

    for name, grades in students.items():
        print(f" {name}:")
        total = 0
        for subject, grade in grades.items():
            print(f" {subject}: {grade}")
            total += grade

        if grades:
            average = student_average(grades)
            print(f" Average: {average:.2f}")
        print()

def subject_summary():
    """Creates a summary for each subject"""
    if not subjects:
        print("No subjects defined")
        return

    print("~~~ Subject Summary ~~~")

    for subject in subjects:
        subject_grades = []
        for name, grades in students.items():
            if subject in grades:
                subject_grades.append(grades[subject])

        if subject_grades:
            highest_grade, lowest_grade, average_grade = subject_stats(subject_grades)
            print(f"{subject}:")
            print(f" Highest Grade: {highest_grade}")
            print(f" Lowest Grade: {lowest_grade}")
            print(f" Average: {average_grade}")
            print(f" Students with grade: {len(subject_grades)}")
        else:
            print(f"No grades recorded for {subject}")

def summary_table():
    """Creates the entire summary table"""
    if not students:
        print("No students in the system")
        return

    print("\n~~~ Student Summary Table ~~~")
    print(f"{'Name':<15}", end="")
    for subject in subjects:
        print(f"{subject:<12}", end="")
    print("Average")

    for name, grades in students.items():
        print(f"{name:<15}", end="")
        total = 0
        valid_subjects = 0

        for subject in subjects:
            grade = grades.get(subject, "N/A")
            if grade != "N/A":
                print(f"{grade:<12}", end="")
                total += grade
                valid_subjects += 1
            else:
                print(f"{'N/A':<12}", end="")

        if valid_subjects > 0:
            average = total/valid_subjects
            print(f"{average:.2f}")
        else:
            print("N/A")

def overall_average():
    """Calculating the overall class average"""
    if not students:
        print("No students in the system")
        return

    total_grade = 0
    total_subjects = 0

    for grades in students.values():
        for grade in grades.values():
            total_grade += grade
            total_subjects += 1

    if total_subjects > 0:
        overall_avg = total_grade/total_subjects
        print(f"Overall Class Average: {overall_avg:.2f}")
        print(f"Based on {total_subjects} grades from {len(students)} students")
    else:
        print("No grades available to calculate the overall average")

def setup_subjects():
    """Subjects for the class"""
    global subjects

    while True:
        try:
            num_subjects = int(input("How many subjects does each student have? "))
            if num_subjects > 0:
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print("PLease enter a valid number")

    for i in range(num_subjects):
        while True:
            subject_name = input(f"Enter subject name {i+1}: ").strip()
            if subject_name:
                if subject_name in subjects:
                    print("This subject already exists")
                else:
                    subjects[subject_name] = []
                    break
            else:
                print("Subject name cannot be empty")

def display_menu():
    """Displays the main menu"""
    print("~~~ Main Menu ~~~")
    print("1. Add New Student")
    print("2. Update Student's Grade")
    print("3. Remove Current Student")
    print("4. Student Grades Profile")
    print("5. Subject Grades Profile")
    print("6. Student Search")
    print("7. Class Report")
    print("8. Subject Summary")
    print("9. Summary Table")
    print("10. Class Overall Average")
    print("11. Exit")

def menu_choice():
    """Get valid menu choice from users"""
    while True:
        try:
            choice = int(input("Enter your choice(1-11): "))
            if 1 <= choice <= 11:
                return choice
            else:
                print("Please enter a number between 1 and 11")
        except ValueError:
            print("Please enter a valid number")

def main():
    """The main program"""
    print("~~~ Student GradeBook Management System ~~~")
    setup_subjects()

    while True:
        display_menu()
        option = menu_choice()

        if option == 1:
            add_students()
        elif option == 2:
            student_grade_update()
        elif option == 3:
            remove_student()
        elif option == 4:
            student_profile()
        elif option == 5:
            subject_profile()
        elif option == 6:
            search_student()
        elif option == 7:
            class_report()
        elif option == 8:
            subject_summary()
        elif option == 9:
            summary_table()
        elif option == 10:
            overall_average()
        elif option == 11:
            print("Adios!")
            break

if __name__ == "__main__":
    main()