students = {}
subjects = {}

def add_students():
    name = input("Please enter the name of the student: ")
    if name in students:
        print("This student already exists")
        return
    students[name] = {}
    print(f"{name} was added successfully")
    for subject in subjects:
        grade = -1
        while grade < 0 or grade > 100:
            grade_input = input(f"Enter marks for {subject}: ")
            try:
                grade = int(grade_input)
                if grade < 0 or grade > 100:
                    print("Grade must range between 0 and 100")
            except ValueError:
                print("Please enter a valid mark")
                grade = -1
        students[name][subject] = grade

def student_grade_update():
    """Updates a specific subject for a student"""
    name = input("Enter the name of the student: ")
    if name not in students:
        print("Specified student was not found")
        return
    print(f"{name}'s subjects:")
    for subject in subjects:
        print(f"{subject}: {students[name].get(subject, 'No record of subject')}")
        subject = input("Enter subject: ")
        if subject not in subjects:
            print(f"Subject not found under{name}")
            return
        grade = -1
        while grade < 0 or grade > 100:
            grade_input = input(f"Enter updated marks for {subject}: ")
            try:
                grade = int(grade_input)
                if grade < 0 or grade > 100:
                    print("The grade should range from 0 to 100")
            except ValueError:
                print("Enter a valid grade")
                grade = -1
        students[name][subject] = grade
        print(f"{subject} was successfully updated")

def remove_student():
    """Removes a specific student from the Gradebook System"""
    name = input("Enter student to be removed: ")
    if name in students:
        del students[name]
        print(f"{name} was successfully removed")
    else:
        print(f"{name} was not found in the system")

def student_profile():
    """Shows a specified student's grades"""
    name = input("Enter the student's name: ")
    if name not in students:
        print(f"{name} not in the system")
        return
    print(f"{name}'s Grades:")
    total = 0
    for subject, grade in students[name].items():
        print(f" {subject}: {grade}")
        total += grade
    if len(students[name])>0:
        average = total / len(students[name])
        print(f"Average: {average:.2f}")

def subject_profile():
    """Shows the grades of a specific subject"""
    subject = input("Enter the name of the subject: ")
    if subject not in subjects:
        print(f"{subject} does not exist")
        return
    print(f"{subject} Grades:")
    subject_grade = []
    for name, grade_dict in students.items():
        if subject in grade_dict:
            grade = grade_dict[subject]
            print(f" {name}: {grade}")
            subject_grade.append(grade)
    if subject_grade:
        highest_grade = max(subject_grade)
        lowest_grade = min(subject_grade)
        subject_average = sum(subject_grade) / len(subject_grade)
        print(f"Highest Grade: {highest_grade}")
        print(f"Lowest Grade: {lowest_grade}")
        print(f"Average: {subject_average}")

def search_student():
    """Searches for a specific student and outputs their info"""
    name = input("Who are you looking for?: ")
    if name in students:
        print(f"{name} was found")
        print("Grades: ")
        total = 0
        for subject, grade in students[name].items():
            print(f" {subject}: {grade}")
            total += grade
        if len(students[name]) > 0:
            average = total / len(students[name])
            print(f"Average: {average:.2f}")
    else:
        print(f"{name} not found")

def class_report():
    """Creates a class report"""
    print("~~~ Class Report~~~")
    for name, grades in students.items():
        print(f" {name}:")
        total = 0
        for subject, grade in grade.items():
            print(f" {subject}: {grade}")
            total += grade
        if len(grades) > 0:
            average = total / len(grades)
            print(f" Average: {average:.2f}")

def subject_summary():
    """Creates a summary for each subject"""
    print("~~~ Subject Summary ~~~")
    for subject in subjects:
        subject_grade = []
        for name, grades in students.items():
            if subject in grades:
                subject_grade.append(grades[subject])
        if subject_grade:
            highest_grade = max(subject_grade)
            lowest_grade = min(subject_grade)
            subject_average = sum(subject_grade) / len(subject_grade)
            print(f"{subject}:")
            print(f"Highest Grade: {highest_grade}")
            print(f"Lowest Grade: {lowest_grade}")
            print(f"Average: {subject_average}")

def summary_table():
    """Creates the entire summary table"""
    print("\n~~~ Student Summary Table ~~~")
    print(f"{'Name':<15}", end="")
    for subject in subjects:
        print(f"{subject:<12}", end="")
    print("Average")

    for name, grades in students.items():
        print(f"{name:<15}", end="")
        total = 0
        for subject in subjects:
            grade = grades.get(subject, "No record of subject")
            print(f"{grade:<12}", end="")
            if grade != "N/A":
                total += grade
        if len(grades) > 0:
            average = total / len(grades)
            print(f"{average:.2f}")
        else:
            print("N/A")

def overall_average():
    """Calculating the overall class average"""
    total_grade = 0
    total_subjects = 0
    for name, grades in students.items():
        for grade in grades.values():
            total_grade += grade
            total_subjects += 1
    if total_subjects > 0:
        overall_average = total_grade / total_subjects
        print(f"Overall Class Average = {overall_average:.2f}")
    else:
        print("You did not enter grades to calculate the overall average")

def setup_subjects():
    """Subjects for the class"""
    global subjects
    num_subjects = int(input("How many subjects does each student have? "))
    for i in range(num_subjects):
        subject_name= input(f"Enter subject name {i+1}: ")
        subjects[subject_name] = []

def main():
    """The main program"""
    print("~~~ Student GradeBook Management System ~~~")
    setup_subjects()
    while True:
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

        option = input("Enter your choice(1-11): ")
        if option == '1':
            add_students()
        elif option == '2':
            student_grade_update()
        elif option == '3':
            remove_student()
        elif option == '4':
            student_profile()
        elif option == '5':
            subject_profile()
        elif option == '6':
            search_student()
        elif option == '7':
            class_report()
        elif option == '8':
            subject_summary()
        elif option == '9':
            summary_table()
        elif option == '10':
            overall_average()
        elif option == '11':
            print("Adios!")
            break
        else:
            print("Enter valid choice")

if __name__ == "__main__":
    main()

