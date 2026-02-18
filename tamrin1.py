# Student name storage program

print("="*40)
print("      STUDENT REGISTRATION PROGRAM")
print("="*40)


# Empty dictionary for students
students = {}

while True:
    print("\nOptions:")
    print("1. Add student")
    print("2. Show all students")
    print("3. Exit")
    print("4.namayesh taedad daneshjuya")
    
    choice = input("\nWhat do you want to do? (1-3): ")
    
    if choice == "1":
        # Get student information
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        
        # Save in dictionary
        students[student_id] = name
        
        print(f" Student {name} with ID {student_id} added!")
    
    elif choice == "2":
        # Show all students
        if len(students) == 0:
            print(" No students yet!")
        else:
            print("\n📋 Student List:")
            print("-"*30)
            for id, name in students.items():
                print(f"ID: {id} -> Name: {name}")
    
    elif choice == "3":
        print("\nGoodbye!")
        break
    
    else:
        print(" Wrong choice! Please select 1, 2, or 3.")