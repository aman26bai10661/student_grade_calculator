students = []

def calculate_grade(marks):
    percentage = sum(marks) / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []
    print("Enter marks of 5 subjects:")

    for i in range(5):
        mark = float(input("Subject " + str(i + 1) + ": "))
        marks.append(mark)

    percentage, grade = calculate_grade(marks)

    student = {
        "name": name,
        "roll": roll_no,
        "marks": marks,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print("\nName:", student["name"])
        print("Roll No:", student["roll"])
        print("Marks:", student["marks"])
        print("Percentage:", round(student["percentage"], 2), "%")
        print("Grade:", student["grade"])


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll No:", student["roll"])
            print("Marks:", student["marks"])
            print("Percentage:", round(student["percentage"], 2), "%")
            print("Grade:", student["grade"])
            return

    print("Student not found.")


def show_result():
    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll_no:
            print("\n========== RESULT ==========")
            print("Name       :", student["name"])
            print("Roll No    :", student["roll"])
            print("Percentage :", round(student["percentage"], 2), "%")
            print("Grade      :", student["grade"])
            print("============================")
            return

    print("Student not found.")


while True:
    print("\n==============================")
    print(" STUDENT GRADE MANAGEMENT")
    print("==============================")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Show Result")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_result()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
