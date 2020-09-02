from django.contrib import admin
from .models import branch,departments,employees

# Register your models here.
admin.site.register(branch)
admin.site.register(departments)
admin.site.register(employees)
