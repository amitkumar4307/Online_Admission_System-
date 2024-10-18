from django.shortcuts import render

# Create your views here.
def studentdash(request):
    return render(request, "studentindex.html")
