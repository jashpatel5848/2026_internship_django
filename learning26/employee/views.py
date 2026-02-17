from django.shortcuts import render,HttpResponse,redirect
from .models import Employee
from .forms import EmployeeForm,CourseForm



# Create your views here.
def employeeList(request):
    #employees = Employee.objects.all()   #select * from employee
    employees = Employee.objects.all().order_by("id").values()
    #employees = Employee.objects.all().values_list()
    print(employees)
    return render(request, 'employee/employeeList.html', {'employees': employees}) 

def employeeFilter(request):
    
    #where select  from employee where name = "raj"
    employee = Employee.objects.filter(name ="raj").values()
    #selet  from employee where post = "Developer"
    employee2 = Employee.objects.filter(post ="developer").values()
    #select  from employee where name = "raj" and post = "Developer"
    employee3 = Employee.objects.filter(name ="raj",post ="hr").values()
    #select  from employee where name = "raj" or post = "Developer"

    #>23
    #select from employee whre age > 23
    employee4 = Employee.objects.filter(age__gt = 23).values()
    employee5 = Employee.objects.filter(age__gte = 23).values()

    #it ,ite

    #strig query
    employee6 = Employee.objects.filter(post__exact = "Developer").values()
    employee7 = Employee.objects.filter(post__iexact = "developer").values()
    #contains
    employee8 = Employee.objects.filter(name__contains = "r").values()
    employee9 = Employee.objects.filter(name__icontains = "R").values()

    #startswith endwith
    employee10 = Employee.objects.filter(name__startswith = "R").values()
    employee11 = Employee.objects.filter(name__endswith = "R").values()
    employee12 = Employee.objects.filter(name__istartswith = "R").values()
    employee13 = Employee.objects.filter(name__iendswith = "R").values()

    #in
    employee14 = Employee.objects.filter(name__in=["raj","jay"]).values()
    #range
    employee15 =Employee.objects.filter(age__range=[24,30]).values()
    #order  by
    employee16 = Employee.objects.order_by("age").values()   #asc
    employee17 = Employee.objects.order_by("-age").values()  #desc

    employee18 = Employee.objects.order_by("-salary").values()   #desc
    



    #end
    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)
    print("query 7",employee7)
    print("query 8",employee8)
    print("query 9",employee9)
    print("query 10",employee10)
    print("query 11",employee11)
    print("query 12",employee12)
    print("query 13",employee13)
    print("query 14",employee14)
    print("query 15",employee15)
    print("query 16",employee16)
    print("query 17",employee17)
    print("query 18",employee18)

    return render(request, 'employee/employeeFilter.html')

def createEmployee(request):
    Employee.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date="2022-01-01")
    return HttpResponse("EMPLOYEE CREATED")

def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() #it same as create
        #return HttpResponse("EMPLOYEE CREATED...")
        return redirect("employeeList")
        
    else:
        #formobject create --> html
        form = EmployeeForm()  #form object
        return render(request,"employee/createEmployeeForm.html",{"form":form})
    


def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST)  #csrf token,form all fields data
        form.save()  #create...insert into table
        return HttpResponse("COURSE CREATED...")
    else:
        form = CourseForm()
        return render(request,"employee/createCourse.html",{"form":form})
    

def deleteEmployee(request,id):
    #delete from employee where id = 1
    print("id from url",id)
    Employee.objects.filter(id=id).delete()
    #HttpResponse("EMPLOYEE DELETED...")
    #employee list redirect
    return redirect("employeeList") #url --> name -->

def filterEmployee(request):
    print("filter employee called...")
    employees = Employee.objects.filter(age__gte=25).values()
    print("filter employees = ",employees)
    return redirect("employeeList")

def updateEmployee(request,id):
    #database existing use ...id -->
    employee = Employee.objects.get(id=id) #select * from employee where id = 1
    form = EmployeeForm(instance=employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        form.save()
        return redirect("employeeList")
    else:
        form = EmployeeForm(instance=employee)
        return render(request,"employee/updateEmployee.html",{"form":form})

        



    


