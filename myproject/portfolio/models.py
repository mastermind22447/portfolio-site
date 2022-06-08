from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category,related_name='post_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
