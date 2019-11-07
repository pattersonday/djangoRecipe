from django.shortcuts import render
from recipeBox.models import RecipeItem 
from recipeBox.models import Author
from recipeBox.forms import NewsAdd, AuthAdd


def index(request):
    html = "index.html"
    recipes = RecipeItem.objects.all()

    return render(request, html, {'data': recipes})

def recipe_item_view(request, key_id):
    html = 'itempage.html'
    
    recipe = RecipeItem.objects.get(pk=key_id)

    return render(request, html, {'data': recipe})

def author_view(request, key_id):
    html = 'author_page.html'

    author = Author.objects.get(pk=key_id)

    items = RecipeItem.objects.all().filter(author=author)

    return render(request, html, {
        'author': author,
        'recipes': items
    })


def news_add(request):
    html ='news.html'
    form = None

    if request.method == 'POST':
        
        form = NewsAdd(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            RecipeItem.objects.create(
                title=data['title'],
                # body=data['body'],
                author=Author.objects.filter(id=data['author']).first()
            )
            return render(request,'thanks.html')


        

    else:
        # everything here is going to be a get request
        form = NewsAdd()
    return render(request, html, {'form': form})




def auth_add(request):
    html = 'auth_Add.html'
    form = None

    if request.method == 'POST':
        form = AuthAdd(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(name=data['name'], bio=data['bio'])

            return render (request, 'thanks.html')
    else:

        form = AuthAdd()

    return render(request, html, {'form': form})