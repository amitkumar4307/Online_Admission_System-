
# Register your models here.
# myapp/admin.py

from django.contrib import admin
from .models import Enquiry,AdminLogin,Student,course


admin.site.register(Enquiry)
admin.site.register(AdminLogin)
admin.site.register(Student)
admin.site.register(course)

