from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    type_choices = (
        ('M', 'Manager'),
        ('N', 'Normal'),
    )
    cname = models.CharField(max_length=25)
    email = models.EmailField(null=False, primary_key=True)
    type = models.CharField(max_length=1, choices=type_choices)
    flag = models.BooleanField(default=True)

    def __str__(self):
        return self.cname


class Profile(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    company = models.ForeignKey(Company, related_name='company_name', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    hobbies = models.CharField(max_length=30)
    picture = models.FileField(upload_to='images/', blank=True, verbose_name="")

    def __str__(self):
        return self.name + ":" + str(self.picture)
