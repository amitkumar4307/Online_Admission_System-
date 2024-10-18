from django.urls import path
from adminapp import views


urlpatterns=[
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('showenq/',views.showenq,name='showenq'),
    path('adminprofile/',views.adminprofile,name='adminprofile'),
    path('addcourse/', views.addcourse,name='addcourse'),
    path('coursedashboard/',views.coursedashboard,name='coursedashboard'),
    path('studentboard/',views.studentboard,name='studentboard'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('courseadd/',views.courseadd,name='courseadd'),
    path('viewcourse/',views.viewcourse,name='viewcourse'),
  
]