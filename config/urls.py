from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

def index(request,number):
    return render(request,"index.html",{"number":number})


urlpatterns = [
    path('admin/', admin.site.urls),
    path("<int:number>/", index),
]
