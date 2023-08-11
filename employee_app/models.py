from django.db import models

# Create your models here.
class Postion(models.Model):
    title=models.CharField(max_length=50)

class Employee(models.Model):
    fullname=models.CharField(max_length=40)
    emp_code=models.CharField(max_length=30)
    mobile=models.CharField(max_length=15)
    postion=models.CharField(Postion,on_delete=models.CASCADE) 