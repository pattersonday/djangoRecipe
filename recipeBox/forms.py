from django import forms
from recipeBox.models import Author
from . import models


# class NewsAdd(forms.Form):
#     title = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea)
#     prepTime = forms.CharField(max_length=50)
#     instructions = forms.CharField(widget=forms.Textarea)
#     author = forms.ModelChoiceField(queryset=Author.objects.all())


class NewsAdd(forms.ModelForm):
    class Meta:
        model = models.RecipeItem
        fields = ['title', 'description', 'prepTime', 'instructions', 'author']


class AuthAdd(forms.Form):

    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
