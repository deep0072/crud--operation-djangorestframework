from django.db import models
from django.db.models.base import Model

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    Roll_No = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self):
        return self.name
