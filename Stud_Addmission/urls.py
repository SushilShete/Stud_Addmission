
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.add_show,name='addshow'),
    path('delete/<int:id>/',views.delete_stud,name='deletedata'),
    path('<int:id>/',views.update_data,name='updatedata'),
    
    path('Students/',views.Show_data,name='alldata'),

 ]