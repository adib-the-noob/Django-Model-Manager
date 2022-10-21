from django.db import models

# Create your models here.
 
# Model Manager
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    is_deleted = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    info = models.TextField()

    object = StudentManager()
    admin_object = models.Manager()

    def __str__(self):
        return self.name