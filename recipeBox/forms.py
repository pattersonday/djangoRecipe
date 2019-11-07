from django import forms
from recipeBox.models import Author

class NewsAdd(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    
    authors = [(a.id, a.name) for a in Author.objects.all()]
    
    author = forms.ChoiceField(choices=authors)



class AuthAdd(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    
    
