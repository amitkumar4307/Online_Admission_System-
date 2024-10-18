from django.urls import path
from studentapp import views


urlpatterns=[
    path('studentapp', views.studentdash, name='studentdash'),
    
 
    
]