from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Indobyte_employees(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=20)
    emp_address = models.TextField()
    emp_salary = models.IntegerField()

    def __str__(self):
        return self.emp_name


class UserDetails(models.Model):
    mobile = models.CharField(max_length=13, null=True)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)

    DEGREE_CHOICES = [
        ('N', 'None'),
        ('M', 'Masters'),
        ('G', 'Graduation'),
        ('D', 'Diploma'),

    ]
    Education = models.CharField(max_length=6, choices=DEGREE_CHOICES, default=None)
    FAVORITE_HOBBIES = [
        ('reading', 'Reading_Books'),
        ('walking', 'Walking'),
        ('playing', 'Playing_Games'),
        ('swimming', 'Swimming'),
        ('listen', 'Listen_Music'),
    ]
