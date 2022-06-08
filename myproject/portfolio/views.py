from multiprocessing import context
from re import template
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
from django.template import loader



def home(request):
    category = Category.objects.all()
    template = loader.get_template('base/home.html')
    
    context = {
        'categories' : category,
    }
    print ("-----------")
    print (category)
    

    return HttpResponse(template.render(context, request))




def projects(request):
    post = Post.objects.all
    template = loader.get_template('base/projects.html')
    
    context = {
        'posts' : post,
    }
    return HttpResponse(template.render(context, request))



def project(request):
    return render(request,'base/project.html')

def about(request):
    return render(request,'base/about.html')

def coding(request):
    return render(request,'base/coding.html')