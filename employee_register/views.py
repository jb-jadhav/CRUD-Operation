from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request):

    context = Employee.objects.all()
    return render(request,'employee_register/employee_list.html',{'context':context})


def employee_form(request, id = 0):

    if request.method == "GET":
        
        if id == 0:
            emp = EmployeeForm()
        
        else:
            employee = Employee.objects.get(pk = id)
            emp = EmployeeForm(instance = employee)
        return render(request, 'employee_register/employee_form.html',{'emp': emp })
    else:
        if id == 0:
            emp = EmployeeForm(request.POST)
        else:
             employee = Employee.objects.get(pk = id)
             emp = EmployeeForm(request.POST,instance = employee)

        if emp.is_valid():
            emp.save()
            
            fullname = emp.cleaned_data['fullname']
            print("name =======>",fullname)  
        return redirect('/employee/list')


def employee_delet(request,id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('/employee/list')

