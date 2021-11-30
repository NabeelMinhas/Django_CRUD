from django.urls import path 
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('edit/<reg_num>/',views.edit, name='edit'), #the <reg_num> is given dynamicallly
    path('dele/<reg_num>/',views.dele, name='dele') 
]
