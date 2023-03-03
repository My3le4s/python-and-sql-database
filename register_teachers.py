from main import Teacher


try:
    teacher_name = input("Enter name: \n")
    teacher_email = input("Enter email: \n")
    teacher_password = input("Enter password: \n")

    Teacher.create(teacher_name=teacher_name, teacher_email=teacher_email, teacher_password=teacher_password)
    print("Teacher Created Successfully")
except:
    print("Failed to Create Teachers")