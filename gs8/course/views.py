from django.shortcuts import render
# Create your views here.

def learn_django(request):
    cname= 'Django'
    duration = '4 months'
    seats = 10
    course_details ={'nm':cname, 'du':seats, 'st':seats}
    return render(request, 'course/courseone.html',course_details)

def learn_python(request):
    return render(request, 'course/coursetwo.html') 