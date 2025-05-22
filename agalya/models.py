from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    Email=models.EmailField()


    def __str__(self):
        retun (self.name)
        