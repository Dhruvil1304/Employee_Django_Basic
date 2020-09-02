from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("departments/<int:branch_id>",views.depart_info,name="departments"),
    path("employees/<int:department_id>",views.employee_info,name="employees")
]