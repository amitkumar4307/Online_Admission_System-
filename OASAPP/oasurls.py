from django.urls import path
from OASAPP import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
   
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('contact/',views.contact,name='contact'),
    path('logcode/',views.logcode,name='logcode'),
    path('Registration/',views.Registration,name='Registration'),
   
]
