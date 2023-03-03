from peewee import *
from os import  path


connection = path.dirname(path.relpath(__file__))
db = SqliteDatabase(path.join(connection, "Sandra.db"))

#creating our first table
class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()

    class Meta:
        database = db

Student.create_table(fail_silently= True)




class Teacher (Model):
    teacher_name = CharField()
    teacher_email = CharField()
    teacher_password = CharField()

    class Meta:
        database = db

Teacher.create_table(fail_silently= True)


class Product(Model):
    Product_price = CharField()
    Product_quantity = CharField()
    Product_description = CharField()
    Product_color = CharField()


    class Meta:
        database = db

Product.create_table(fail_silently= True)




class User(Model):
    User_name = CharField()
    User_phone = CharField()
    User_email = CharField()
    User_password = CharField()


    class Meta:
        database = db

User.create_table(fail_silently= True)

