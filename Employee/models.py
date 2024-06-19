from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.AutoField(primary_key=True)
    phone= models.BigIntegerField(max_length=12)
    address = models.CharField(max_length=200)
    working = models.CharField(max_length=12)
    department = models.CharField(max_length=150)
    