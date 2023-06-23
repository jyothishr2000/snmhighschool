from django.db import models


SUBJECT_LIST=(
    ('Science','Science'),
    ('Commerce','Commerce'),
    ('Humanities','Humanities')
)

class student(models.Model):
    ad_no=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=200)
    subject=models.CharField(max_length=20,choices= SUBJECT_LIST)
    gname=models.CharField(max_length=100)
    dob=models.DateField()
    contact=models.CharField(max_length=13)
    email=models.EmailField()
    def __str__(self):
        return self.name

class message1(models.Model):
    id=models.IntegerField(primary_key=True)
    comment=models.CharField(max_length=500)

class message2(models.Model):
    id=models.IntegerField(primary_key=True)
    enquire=models.CharField(max_length=500)
