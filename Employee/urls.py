from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [ 
    
    path('home/',Emp_home),
    path('add_emp/',Add_emp),
    path('delete_emp/<int:emp_id>',Delete_emp),
    path('update_emp/<int:emp_id>',Update_emp),
    path('do_update_emp/<int:emp_id>',Do_update_emp),
    path('about/',about),
    
]
