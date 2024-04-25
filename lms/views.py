from django.shortcuts import render
from lms_admin.models import Course

def index(request):
    return render(request, 'index.html')

def blogs(request):
    return render(request, 'blogs.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', context={'courses' : courses})

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def course_detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'course_detail.html', context={'course' : course})