from django.contrib import admin
from crud.models import Student

# Register your models here.
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
