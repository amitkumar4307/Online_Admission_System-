from django.db import models

# Create your models here.

    
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)
    
class AdminLogin(models.Model):
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    

    
class course(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    course_session=models.CharField(max_length=30)
    course_name=models.CharField(max_length=300)
    course_fees=models.CharField(max_length=100)
    course_date=models.DateTimeField(auto_now_add=True)
    
class Student(models.Model):
    sid=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=50)
    emailaddress=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    contactno=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    dob=models.CharField(max_length=30)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    address=models.TextField()
    adhaarno=models.CharField(max_length=15)
    aadharpic=models.ImageField(upload_to='')
    session=models.CharField(max_length=20)
    course=models.CharField(max_length=30)
    hs_percent=models.CharField(max_length=10)
    hs_marksheet=models.ImageField(upload_to='')
    interpercent=models.CharField(max_length=10)
    intermarksheet=models.ImageField(upload_to='')
    pic=models.ImageField(upload_to='')
    signature=models.ImageField(upload_to='')
    application_status=models.CharField(max_length=1)
    fees=models.IntegerField()
    fees_status=models.CharField(max_length=1)
    fees_ss=models.ImageField(upload_to='')
    status=models.CharField(max_length=1)
    
    
    
    
    
    
    
    
    
    