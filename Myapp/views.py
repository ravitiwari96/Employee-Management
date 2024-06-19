from django.http import HttpResponse
from django.shortcuts import render
import datetime



def home(request):
     
    if request.method == "POST":
        check = request.POST['check']
        print(check)
    
    
    
    # date = datetime.datetime.now()
    print("Test function is called from view")
    name = "Ravi Tiwari"
    isActive = True
    list_of_programs = {
        "WAP to check prime or not",
        "WAP to check even or odd",
        "WAP to check armstong number",
        "WAP to check palindrome string"
    }
    student_data = {
        "student_name" : "Ravi Tiwari",
        "student_college" : "SVIM",
        "student_address" : "Indore"
    }
    
    data = {
        "isActive": isActive,
        "name" : name,
        "list_of_programs": list_of_programs,
        "student_data" : student_data   
    }
    # return HttpResponse("<h1>Hello this is index page<h1/>"+str(date))
    return render(request,"home.html",data)

def about(request):
    # return HttpResponse("<h1>This is a about page<h1/>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1>This is a services page<h1/>")
    return render(request,"services.html",{}) 