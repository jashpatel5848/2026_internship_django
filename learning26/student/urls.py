from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.studenthome),
    path("dashboard/",views.studentdashboard),
    path("list/",views.studentlist),
    
]    