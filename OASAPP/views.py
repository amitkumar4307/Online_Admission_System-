from django.shortcuts import render,redirect
from .models import Enquiry,AdminLogin,course,Student
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, "index.html")

def studentlogin(request):
    return render(request,"studentlogin.html")

def admindashboard(request):
    return render(request,'admindashboard.html')


def contact(req):
    if req.method=="POST":
        name=req.POST["name"]
        gender=req.POST["gender"]
        address=req.POST["address"]
        contactno=req.POST["contactno"]
        emailaddress=req.POST["emailaddress"]
        enquirytext=req.POST["enquirytext"]
        enquirydate=req.POST["enquirydate"]
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        msg="Your form send successfully !"
        return render(req,'contact.html',{'msg':msg})
    return render(req, 'contact.html')

def logcode(req):
    if req.method=="POST":
        adminType=req.POST['adminType']
        user=req.POST['user']
        password=req.POST['password']
        if adminType=='admin':
            try:
                user=AdminLogin.objects.get(user=user,password=password)
                if user is not None:
                    req.session['adminid']=user.user
                    return redirect('adminapp:admindashboard')
            except ObjectDoesNotExist:
                return render(req,'studentlogin.html',{'msg':'Invalid user'})
        elif adminType=="student":
            try:
                stu=Student.objects.get(emailaddress=user,password=password)
                if stu is not None:
                    req.session['studentid']=user
                    return redirect('studentapp:studentdash')
            except ObjectDoesNotExist:
                return render(req,'studentlogin.html',{'msg':'Invalid user'})
                
                
                
def Registration(req):
    return render(req, 'Registration.html')
