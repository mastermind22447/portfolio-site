from django.contrib import admin
from .models import Post, Category

@admin.register(Post, Category)
class PostAdmin(admin.ModelAdmin):
    pass
