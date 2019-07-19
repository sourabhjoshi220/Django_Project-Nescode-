from django.db import models

# Create your models here.

class customer(models.Model):
    Name=models.CharField(max_length=30)
    Add=models.CharField(max_length=30)
    Phone_no=models.IntegerField()
    Email=models.CharField(max_length=30)

class investment(models.Model):
    Customer_Name=models.CharField(max_length=30)
    Amount=models.IntegerField()
    Investment_Type=models.CharField(max_length=30)



