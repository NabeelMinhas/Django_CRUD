from django.contrib import admin
from .models import student
# Register your models here.

class stuadmin(admin.ModelAdmin):
    fields =['reg_num','name','degree']

admin.site.register(student,stuadmin)