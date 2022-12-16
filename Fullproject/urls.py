from django.contrib import admin
from django.urls import path, include
from application import views

urlpatterns = [
    path('gradesApp/',include('application.urls')),
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('logout/',views.userLogout,name='logout'),
    path('studentDash/',views.studentDash,name='studentDash'),
    path('teacherDash/',views.teacherDash,name='teacherDash'),
    path('employeeDash/',views.employeeDash,name='employeeDash'),

]

admin.site.site_header  =  "Marc2Lab Administration"
admin.site.site_title  =  "2 Marc2Lab admin site"
admin.site.index_title  =  "Marc2Lab Admin"