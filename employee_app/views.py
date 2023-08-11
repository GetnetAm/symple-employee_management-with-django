from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
# def home(request):
#     return render(request, 'employee_app/home.html')

def employee_list(request):
    return render(request, 'employee_app/employee_list.html')

def employee_form(request):
    
    form=EmployeeForm()
    return render(request, 'employee_app/employee_form.html', {'form':form})

def employee_delete(request):
    return
    