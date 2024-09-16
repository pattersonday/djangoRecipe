"""
author  
    name 
    bio

recipeItem
    title
    description 
    prepTime
    instructions
    Author
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    bio = models.TextField()
    favorites = models.ManyToManyField('RecipeItem', blank=True, related_name='favorites')

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    prepTime = models.CharField(max_length=50)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} - {self.author.name}'
