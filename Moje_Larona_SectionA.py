total_grade = 0
student = []

num_students = int(input("How many students are in your class? "))
for i in range(num_students):
        student_name = input(f"\nEnter name for student {i + 1}: ")

        grade = -1
        while grade < 0 or grade > 100:
            grade_input = input(f"Enter marks for (0-100): ")
            try:
                grade = int(grade_input)
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
                grade = -1

        student.append((student_name, grade))
        total_grade += grade

print("\n~~~ Class Report ~~~")
for name, grade in student:
    print(f"{name}: {grade}")

average_marks = total_grade / num_students
print(f"Overall Class Average = {average_marks:.2f}\n")