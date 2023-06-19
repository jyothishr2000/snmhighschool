from django.db import models

class student(models.Model):
    ad_no=models.IntegerField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=200)
    subject=models.CharField("Science","Commerce","Humanities")
    gname=models.CharField(max_length=100)
    dob=models.DateField()
    contact=models.IntegerField()
    email=models.EmailField()

# Create your models here.
