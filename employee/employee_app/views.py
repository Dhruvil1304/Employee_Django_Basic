from django.shortcuts import render
from django.urls import reverse
from .models import branch,departments,employees
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    branches=branch.objects.all()
    return render(request,'employee_app/index.html',{
        "brn":branches
    })

def depart_info(request,branch_id):
    branchdetail=branch.objects.get(pk=branch_id);
    departs=branchdetail.departs.all()
    return render(request,'employee_app/departs.html',{
        "depts":departs
    })

def employee_info(request,department_id):
    department_details=departments.objects.get(pk=department_id)
    employeee=department_details.workers.all()
    return render(request,'employee_app/emp.html',{
        "emps":employeee
    })