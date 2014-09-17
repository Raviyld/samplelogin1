from django.db import models
import os

# Create your models here.

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class User(models.Model):
    Username = models.CharField(max_length = 30, unique=True)
    Password = models.CharField(max_length = 30)
    DOB = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length = 30, choices=GENDER_CHOICES)
    Mobile = models.IntegerField(null=True, blank = True)
    Mail = models.EmailField()
    class Admin:
        pass
    def __str__(self):
        return '%s''--''%s' %(self.Username,self.Gender)
        
class Loginlog(models.Model):
    Username = models.ForeignKey(User)
    Logindate = models.DateTimeField(auto_now=True, null=True, blank = True)
    class Admin:
        pass
    def __str__(self):
        return '%s'%(self.Logindate)