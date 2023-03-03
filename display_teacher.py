
from main import Teacher

Teachers = Teacher.select()
for Teacher in Teachers :
    print(Teacher.teacher_name, Teacher.teacher_email, Teacher.teacher_password)