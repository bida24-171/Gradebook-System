total_grade = 0
students = []

#Input the number of students and subjects
num_students = int(input("How many students are in your class? "))
num_subjects = int(input("How many subjects does each student have? "))

subjects = [] # new list for subjects
for i in range(num_subjects):
    subject_name = input(f"\nEnter subject name {i+1}: ")
    subjects.append(subject_name)

for i in range(num_students):
    student_name = input(f"\nEnter student's name {i+1}: ")
    grades = []

    for j in range(num_subjects):
        grade = -1
        while grade < 0 or grade > 100:
            grade_input = input(f"Enter marks for {subjects[j]} (0-100): ")
            try:
                grade = int(grade_input)
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100!")
            except ValueError:
                print("Please enter a valid mark!")
                grade = -1

        grades.append(grade)
        total_grade += grade

    students.append((student_name, grades))

# Student Reports
print("\n~~~ Class Report ~~~")
for name, grades in students:
    student_average = sum(grades) / len(grades)
    print(f"\n{name}:")
    for i in range(len(grades)):
        print(f" {subjects[i]}: {grades[i]}")
    print(f" Average: {student_average:.2f}")

# Subject Stats
print("\n~~~ Subject Summary ~~~")
for i in range(num_subjects):
    subject_grades = [stu[1][i] for stu in students]
    highest_grade = max(subject_grades)
    lowest_grade = min(subject_grades)
    subject_average = sum(subject_grades) / len(subject_grades)

    print(f"\n{subjects[i]}:")
    print(f" Highest Grade: {highest_grade}")
    print(f" Lowest Grade: {lowest_grade}")
    print(f" Average: {subject_average:.2f}")

# Class Average
overall_average = total_grade / (num_students * num_subjects)
print(f"\nOverall Class Average = {overall_average:.2f}")

# Entire Summary Table
print("\n~~~ Student Summary Table ~~~")
print(f"{'Name':<15}", end="")
for sub in subjects:
    print(f"{sub:<12}", end="")
print("Average")

for name, grades in students:
    student_average = sum(grades) / len(grades)
    print(f"{name:<15}", end="")
    for g in grades:
        print(f"{g:<12}", end="")
    print(f"{student_average:.2f}")
