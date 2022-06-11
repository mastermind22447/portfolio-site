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

def category(request, category_id):
    posts = Post.objects.filter(category_id=category_id).order_by('id')
    category = Category.objects.get(id=category_id)

    context = {
        'posts' : posts,
        'category': category,
    }

    template = loader.get_template('base/projects.html')
    return HttpResponse(template.render(context, request))
    # if category_id == 2:
    #     template = loader.get_template('base/projects.html')
    #     return HttpResponse(template.render(context, request))
   
    # else:
    #     template = loader.get_template('base/coding.html')
    #     return HttpResponse(template.render(context, request))
  


def projects(request):
    post = Post.objects.all
    template = loader.get_template()
    
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