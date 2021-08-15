from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    rollno = models.IntegerField()

    def __str__(self):
        return self.firstname
