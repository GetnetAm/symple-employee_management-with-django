from django.urls import path
from employee_app import views

urlpatterns = [
    path('form', views.employee_form),
    path('list', views.employee_list),
]
