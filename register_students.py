from main import Student


try:
    student_name = input("Enter name: \n")
    student_email = input("Enter email: \n")
    student_password = input("Enter password: \n")

    Student.create_table(stud_name=student_name, stud_email=student_email, stud_password=student_password)
    print("Student Created Successfully")
except:
    print("Failed to Create Students")