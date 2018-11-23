
from django.db import models
from django.contrib.auth.models import Permission, User
from django.urls import reverse



class faculty(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=30, default="NULL")
    branch = models.CharField(max_length=10, default="NULL")
    facid = models.CharField(max_length=10, default="NULL")




class Student(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=30,default="NULL")
    branch=models.CharField(max_length=10,default="NULL")
    usn=models.CharField(max_length=10,default="NULL")
    facid=models.ForeignKey(faculty,default=1,on_delete=models.CASCADE)
    approved=models.BooleanField(default=False)
    issue = models.CharField(max_length=100)
    subject = models.CharField(max_length=100 )
    is_faculty = models.BooleanField(default=False)
    is_dept = models.BooleanField(default=False)


"""class issue(models.Model):
    studentid=models.ForeignKey(Student,default=0,on_delete=models.CASCADE)
    faculty=models.ForeignKey(faculty,default=0,on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="NULL")
    branch = models.CharField(max_length=10, default="NULL")
    usn = models.CharField(max_length=10, default="NULL")
    facname=models.CharField(max_length=30,default="NULL")
    issue=models.CharField(max_length=100,default="NULL")
    subject = models.CharField(max_length=100, default="NULL")
    is_faculty = models.BooleanField(default=False)
    is_dept = models.BooleanField(default=False)"""




