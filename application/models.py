from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# superadmin, admin, administrator, employees, agent 

class Admin(models.Model):
    admin=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    branch=models.CharField(max_length=256,blank=False)
    is_student=models.BooleanField(default=True)

    def __str__(self):
        return self.admin.username


class Administrator(models.Model):
    administrator=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    branch=models.CharField(max_length=256,blank=False)
    is_student=models.BooleanField(default=True)

    def __str__(self):
        return self.administrator.username

class Employee(models.Model):
    employee_name=models.OneToOneField(User,on_delete=models.CASCADE)
    employee_text=models.CharField(max_length=256,blank=False)
    phone=models.IntegerField()
    is_employee=models.BooleanField(default=False)

    def __str__(self):
        return self.employee_name.username

class Agent(models.Model):
    agent=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    branch=models.CharField(max_length=256,blank=False)
    is_student=models.BooleanField(default=True)


    user_id=models.IntegerField()
    lab_code=models.CharField(max_length=256)
    role=models.CharField(max_length=256)


    def __str__(self):
        return self.agent.username

# ----------------------------------------------------------

class Student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    branch=models.CharField(max_length=256,blank=False)
    is_student=models.BooleanField(default=True)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher=models.OneToOneField(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=256,blank=False)
    phone=models.IntegerField()
    is_student=models.BooleanField(default=False)

    def __str__(self):
        return self.teacher.username

