# Student Management System

# List to store all student records (as dictionaries)
students = []

def display_menu():
    print("\n" + "="*35)
    print(" 🎓 Student Management System 🎓")
    print("="*35)
    print("1. Add New Student")
    print("2. View All Student Records")
    print("3. Search for a Student")
    print("4. Update Existing Student")
    print("5. Delete a Student Record")
    print("6. Exit")
    print("="*35)

def add_student():
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ")
    
    # Check if ID already exists
    for student in students:
        if student['ID'] == student_id:
            print("Error: A student with this ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    # Create a dictionary for the new student
    new_student = {
        'ID': student_id,
        'Name': name,
        'Age': age,
        'Course': course,
        'Marks': marks
    }
    
    # Add the dictionary to our list
    students.append(new_student)
    print(f"✅ Student {name} added successfully!")

def view_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No student records found.")
        return
    
    for student in students:
        print(f"ID: {student['ID']} | Name: {student['Name']} | Age: {student['Age']} | Course: {student['Course']} | Marks: {student['Marks']}")

def search_student():
    print("\n--- Search Student ---")
    search_term = input("Enter Student ID or Name to search: ").lower()
    
    found = False
    for student in students:
        if search_term == student['ID'].lower() or search_term in student['Name'].lower():
            print("\n✅ Student Found:")
            print(f"ID: {student['ID']}")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Course: {student['Course']}")
            print(f"Marks: {student['Marks']}")
            found = True
            
    if not found:
        print("❌ No student found matching that ID or Name.")

def update_student():
    print("\n--- Update Student Details ---")
    student_id = input("Enter the ID of the student you want to update: ")
    
    for student in students:
        if student['ID'] == student_id:
            print(f"Updating details for {student['Name']} (Leave blank to keep current value):")
            
            new_name = input(f"Enter new Name [{student['Name']}]: ")
            if new_name: student['Name'] = new_name
            
            new_age = input(f"Enter new Age [{student['Age']}]: ")
            if new_age: student['Age'] = new_age
                
            new_course = input(f"Enter new Course [{student['Course']}]: ")
            if new_course: student['Course'] = new_course
                
            new_marks = input(f"Enter new Marks [{student['Marks']}]: ")
            if new_marks: student['Marks'] = new_marks
                
            print("✅ Student details updated successfully!")
            return
            
    print("❌ Student ID not found.")

def delete_student():
    print("\n--- Delete Student Record ---")
    student_id = input("Enter the ID of the student you want to delete: ")
    
    for i in range(len(students)):
        if students[i]['ID'] == student_id:
            deleted_name = students[i]['Name']
            del students[i]
            print(f"✅ Record for {deleted_name} deleted successfully!")
            return
            
    print("❌ Student ID not found.")

# Main Program Loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Start the program
if __name__ == "__main__":
    main()
