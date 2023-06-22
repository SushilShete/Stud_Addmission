from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from crud.models import Student

# Create your views here.
#this function will add new item and show all item
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration() 
    stud = Student.objects.all() 
    return render(request,'crud/addshow.html',{'form':fm,'stu':stud})

# this function will show all student data
def Show_data(request):
    stud = Student.objects.all()
    return render(request,'crud/all_stud.html',{'stu':stud})
# this function will update or edit
def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)    
    return render(request,'crud/update.html',{'form':fm})

#this function will delete item
def delete_stud(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')

