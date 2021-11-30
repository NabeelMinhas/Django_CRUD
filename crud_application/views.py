from django.shortcuts import render 
from django.http import HttpResponse
from .models import student
# Create your views here.

#adding element
def add(request):
    # form post request receive here
    if request.method=="POST":
        nam=request.POST.get("name")
        reg=request.POST.get("reg_num")
        degr=request.POST.get("degree")
        stu=student(reg_num=reg, name=nam, degree=degr)
        stu.save()
    
    # the table data goes from there
    object=student.objects.all()
    obj={'object':object}
    return render(request, 'main_page.html', obj)

def edit(reques, reg_num):
   #edit form post section
    if request.method=='POST':
        nam=request.POST.get("name")
        reg=request.POST.get("reg_num")
        degr=request.POST.get("degree")
        stu=student(reg_num=reg, name=nam, degree=degr)
        stu.save()   
        object=student.objects.all()
        obj={'object':object}
        return render(request, 'main_page.html', obj)
    
    # the table data goes from there
    object=student.objects.all()
    stu=student.objects.get(reg_num=reg_num) # for edit data send to form section of template
    return render(request, 'main_page.html', {'st':stu , 'object':object})


def dele(request, reg_num):
    #delete object section
    student.objects.filter(reg_num=reg_num).delete() # just this line delete the record
    
    #the table data go from there
    object=student.objects.all()
    obj={'object':object}
    
    return render(request, 'main_page.html', obj)