from django.shortcuts import render, redirect
from employee_register.forms import EmployeeForm
from employee_register.models import Employee

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees})
def delete(request,id):
    employees=Employee.objects.get(id=id)
    employees.delete()
    return redirect('/show')
def edit(request,id):
    emplo=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':emplo})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})