from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.CharField(max_length=100)
