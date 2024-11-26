students={}
def add_students():
    student_id=input("Enter student ID:")
    
    if student_id in students:
        print("student id alredy existe!")
    else:
        name=input("Enter student name:")
        age=input("Enter age:")
        course=input("Enter course:")
        students[student_id]={"Name":name,"Age":age,"Course":course}
        print("student added succesfully",students[student_id])
    


def view_students():
    if not students:
        print("No students to display")
    else:
        print("student records")


        for student in students:
            
            print(student)



def update_students():
    student_id=input("Enter student ID to update: ")
    if student_id in students:
        print("1.update name")
        print("2.update age")
        print("3.update course")
        choice=input("Enter your  update choise:")
        if choice=='1':
            students[student_id]["name"]=input("Enter new name:")
        elif choice=='2':
            srudents[student_id]["age"]=input("Enter new age:")
        elif choice=='3':
            students[student_id]['course']=input("Enter new course:")
        else:
            print("Invalid choice")
        print("Student record updated successfully")
    else:
        print("Student id not found")


def delete_student():
    student_id=input("Enter student ID to delete :")
    if student_id in students:
        del students[student_id]
        print("student deleted successfully")
    else:
        ("student id Not found")



def menu():
    while True:
        print("\n student management system")
        print("1.add student")
        print("2.view student")
        print("3.update student")
        print("4.delete student")
        print("5.Exit")
        choice=input("Enter your choice:")
        if choice=='1':
            add_students()
        elif choice=='2':
            view_students()
        elif choice=='3':
            update_students()
        elif choice=='4':
            delete_student()
        elif choice=='5':
            print('Exiting......')
            break
        else:
            print("Invalid choice! please try again!")
menu()            
            
        
    
