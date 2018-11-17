from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,default="NULL")
    branch=models.CharField(max_length=10,default="NULL")
    usn=models.CharField(max_length=10,default="NULL")
    issue=models.CharField(max_length=100,default="NULL")
    approved=models.BooleanField(default=False)

class faculty(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="NULL")
    branch = models.CharField(max_length=10, default="NULL")
    facid = models.CharField(max_length=10, default="NULL")
