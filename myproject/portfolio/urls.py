from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/<int:category_id>/', views.projects, name='projects'),
    path('architecture/', views.project, name='architecture'),
    path('about/', views.about, name='about'),
    path('coding/', views.coding, name='coding'),

]