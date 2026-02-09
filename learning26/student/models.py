from django.db import models

# Create your models here.
#python class

#parent class model
#create table student(studentname varchar(100),studentage int,stuentcity varchar(40))
#it will generate pk  automatically

class Student(models.Model):
    studentname = models.CharField(max_length=100)
    studentage = models.IntegerField()
    studentcity = models.CharField(max_length=40)
    studentemail = models.EmailField(null=True)
    
    #meta class
    class Meta:
        db_table = "student" #table name

class Product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.IntegerField()
    productdescription = models.TextField()
    productstock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)


    class Meta:
        db_table = "product"

