from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# View to display the home page with a list of employees
def Emp_home(request):
    emps = Employee.objects.all()  # Fetch all employee records
    return render(request, 'Emp/home.html', {'emps': emps})

# View to add a new employee
def Add_emp(request):
    if request.method == "POST":
        # Data fetch from the request
        emp_id = request.POST.get("emp_id")
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_working = request.POST.get("emp_working")

        # Create model object and set the data
        e = Employee()
        e.emp_id = emp_id  # Make sure 'emp_id' is a field in your model
        e.name = emp_name
        e.phone = emp_phone
        e.address = emp_address 
        e.department = emp_department
        e.working = emp_working

        # Save the object
        e.save()
        
        return redirect("/Emp/home/")
    
    return render(request, "Emp/Add_Emp.html", {})


def Delete_emp(request, emp_id):
    emp = Employee.objects.get(emp_id=emp_id)  # Fetch using the correct field
    emp.delete()
    return redirect('/Emp/home/')

def Update_emp(request, emp_id):
    emp = Employee.objects.get(emp_id = emp_id)  # Fetch using the correct field
    return render(request, 'Emp/Update_emp.html',{'emp':emp})

def Do_update_emp(request, emp_id):
    if request.method == "POST":
        
        # Update fields
        emp_id_main = request.POST.get("emp_id")
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_working = request.POST.get("emp_working")
        
        emp = Employee.objects.get(pk=emp_id)
        emp.emp_id = emp_id_main  # Make sure 'emp_id' is a field in your model
        emp.name = emp_name
        emp.phone = emp_phone
        emp.address = emp_address 
        emp.department = emp_department
        emp.working = emp_working

        # Save the updated object
        emp.save()
        
    return redirect("/Emp/home/")

def about(request):
    return render(request,"Emp/about.html")