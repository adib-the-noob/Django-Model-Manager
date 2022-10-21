from django.db import models

# Create your models here.
 

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    info = models.TextField()

    def __str__(self):
        return self.name