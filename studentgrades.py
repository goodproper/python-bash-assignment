# Student Grades Program
students = {}

while True:
    print("\n1. Add student")
    print("2. Update student grade")
    print("3. Print all students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added!")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated!")
        else:
            print("Student not found.")

    elif choice == "3":
        if not students:
            print("No students added yet.")
        else:
            for name, grade in students.items():
                print(name, ":", grade)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
