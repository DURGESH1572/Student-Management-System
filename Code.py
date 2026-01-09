students = []

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    marks = int(input("Enter Marks: "))
    students.append({"ID": sid, "Name": name, "Dept": dept, "Marks": marks})
    print("Student added successfully")

def view_students():
    if not students:
        print("No records found")
        return
    for s in students:
        print(s)

def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s["ID"] == sid:
            print(s)
            return
    print("Student not found")

def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["ID"] == sid:
            s["Name"] = input("Enter new name: ")
            s["Dept"] = input("Enter new department: ")
            s["Marks"] = int(input("Enter new marks: "))
            print("Student updated")
            return
    print("Student not found")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            print("Student deleted")
            return
    print("Student not found")

while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    choice = input("Enter choice: ")
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
        break
    else:
        print("Invalid choice")
