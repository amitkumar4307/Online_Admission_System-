from django.shortcuts import render,redirect
from OASAPP.models import Enquiry,course,Student
from datetime import datetime 
from django.utils import timezone

def admindashboard(request):
    try:
        if request.session['adminid']!=None:     
            return render(request, "admindashboard.html")
    except KeyError:
        return render(request,'studentlogin.html')

def showenq(request):
    enq=Enquiry.objects.all()
    return render(request, "showenq.html",{'enq':enq})
def adminprofile(request):
    return render(request,"adminprofile.html")

def addcourse(req):
    ch=course.objects.all()
    return render(req, 'adminparent.html',{"ch":ch})

def editc(request,id):
    edit=course.objects.get(empid=id)
    return render(request,"editcourse.html",{"edit":edit})
def coursedashboard(req):
    return render(req,'coursedashboard.html')
def studentboard(req):
    return render(req,'studentboard.html')
def addstudent(req):
    if req.method=="POST":
        name=req.POST["name"]
        emailaddress=req.POST["emailaddress"]
        contactno=req.POST["contactno"]
        gender=req.POST["gender"]
        stu=Student(name=name,emailaddress=emailaddress,contactno=contactno,gender=gender,password="12345",fees=0)
        stu.save()
        return redirect('adminapp:addstudent')
    return render(req,'addstudent.html')
def courseadd(req):
    ph=course.objects.all()
    if req.method=="POST":
        
        course_session=req.POST['course_session']
        course_name=req.POST['course_name']
        course_fees=req.POST['course_fees']
        course_date_str = req.POST['course_date']  # This should be in the format 'YYYY-MM-DD'
        course_date = timezone.datetime.strptime(course_date_str, '%Y-%m-%d')
        s=course(course_session=course_session,course_name=course_name,course_fees=course_fees,course_date=course_date)
        s.save()
        return redirect('adminapp:courseadd')
    return render(req,'courseadd.html',{"ph":ph})
def viewcourse(request):
    courses = course.objects.all()  # Get all courses from the database
    return render(request, 'viewcourse.html', {'courses': courses})



  
      



    