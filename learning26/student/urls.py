from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.studenthome),
    path("dashboard/",views.studentdashboard),
    path("list/",views.studentlist),
    path("servicesList/",views.serviceList,name="serviceList"),
    path("createService/",views.createService,name="createService"),
    path('deleteService/<int:id>/', views.deleteService, name='deleteService')

    
]    