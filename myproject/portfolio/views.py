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
    # print ("-----------")
    # print (category)
    

    return HttpResponse(template.render(context, request))



def projects(request, category_id):
    posts = Post.objects.filter(category_id=category_id).order_by('id')
    category = Category.objects.get(id=category_id)

    context = {
        'posts' : posts,
        'category': category,
    }
    
    template = loader.get_template('base/projects.html')

    # print ("-----------")
    # print (category)
    return HttpResponse(template.render(context, request))



def architecture(request):

    return render(request,'base/architecture.html')

def coding(request):
    return render(request,'base/coding.html')

def about(request):
    return render(request,'base/about.html')

