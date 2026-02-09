from django.shortcuts import render

# Create your views here.

def studenthome(request):
    return render(request,'studenthome.html')


def studentdashboard(request):
    student = {"name":"jash","age":22,"city":"ahmedabad"}
    return render(request,"student/studentdashboard.html",student)


def studentlist(request):
    students = [
               {"id":101,"name":"jash","course":"django"},
               {"id":102,"name":"manan","course":"java"},
               {"id":103,"name":"nikhil","course":"react"}
    ]
    return render(request,'student/studentlist.html',{'students':students})
    #student/studentDashboard.html
    #folder/filename