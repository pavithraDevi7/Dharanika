from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    email=models.EmailField()


    def __str__(self):
        retun (self.name)

class biodata(models.Model):
    dept=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=50,null=True,blank=True)
    stream=models.CharField(max_length=50,null=True,blank=True)
        