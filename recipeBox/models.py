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

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name

class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    prepTime = models.CharField(max_length=50)
    instructions = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.title}-{self.author.name}'

