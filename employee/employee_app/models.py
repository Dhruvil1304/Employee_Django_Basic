from django.db import models

# Create your models here.
class branch(models.Model):
    branch_area=models.CharField(max_length=30)
    def __str__(self):
        return f" {self.branch_area} BRANCH"

class departments(models.Model):
    department_name=models.CharField(max_length=64)
    department_timing=models.IntegerField()
    department_branch=models.ManyToManyField(branch,related_name='departs')
    def __str__(self):
        return f" {self.department_name}"

class employees(models.Model):
    employee_fname=models.CharField(max_length=30)
    employee_lname=models.CharField(max_length=30)
    employee_add=models.CharField(max_length=20)
    employee_dept=models.ManyToManyField(departments,related_name='workers')

    def __str__(self):
        return f" {self.employee_fname} {self.employee_lname}"

