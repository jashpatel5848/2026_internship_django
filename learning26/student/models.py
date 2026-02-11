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
    def __str__(self):
        return self.studentname


class Product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.IntegerField()
    productdescription = models.TextField()
    productstock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)


    class Meta:
        db_table = "product"
    def __str__(self):
        return self.product
    

class Studentprofile(models.Model):
    hobbies = (("reading","reading"),("travel","travel"),("music","music"))
    #studnetProfile id --> pk key auto
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studenthobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentphone = models.CharField(max_length=10)
    studentgender = models.CharField(max_length=10)
    studentdob = models.DateField()

    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentname
    

    #cat ---> service

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.categoryName
    
class Service(models.Model):
    serviceName = models.CharField(max_length=100)    
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table cretion adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)


    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName



          

       