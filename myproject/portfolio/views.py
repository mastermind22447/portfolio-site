from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request,'base/home.html')

def projects(request):
    return render(request,'base/projects.html')

def project(request):
    return render(request,'base/project.html')

def about(request):
    return render(request,'base/about.html')

def coding(request):
    return render(request,'base/coding.html')