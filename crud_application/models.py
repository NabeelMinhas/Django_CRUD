from django.db import models

# Create your models here.

class student(models.Model):
    deg=(('1','BS-CS'),('2','BS-civil'),)
    reg_num= models.CharField(max_length=30, primary_key=True)
    name= models.CharField(max_length=100)
    degree=models.CharField(max_length=1,choices=deg)
