from django.shortcuts import redirect, render, get_object_or_404
from .models import Service
from .forms import ServiceForm

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


def serviceList(request):
    services = Service.objects.all()
    return render(request,'student/serviceList.html',{'services':services})



def createService(request):

    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('serviceList')
        else:
            return render(request,"student/createService.html",{'form':form})
        
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{'form':form})
    

    
def deleteService(request, id):
    service = get_object_or_404(Service, id=id)

    if request.method == "POST":
        service.delete()
        return redirect('serviceList')

    return render(request, 'student/confirmDeleteService.html', {'service': service})    
    
