from django.shortcuts import render, HttpResponseRedirect, reverse
from recipeBox.models import Author, RecipeItem
from recipeBox.forms import NewsAdd, AuthAdd, LoginForm
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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


@login_required
def news_add(request):
    html = 'news.html'
    form = None

    if request.method == 'POST':
        form = NewsAdd(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            RecipeItem.objects.create(
                title=data['title'],
                description=data['description'],
                prepTime=data['prepTime'],
                instructions=data['instructions'],
                post_date=timezone.now(),
                # body=data['body'],
                author=data['author']
            )
            return render(request, 'thanks.html')

    else:
        # everything here is going to be a get request
        form = NewsAdd()
    return render(request, html, {'form': form})


@login_required
def auth_add(request):
    html = 'auth_Add.html'

    if request.method == 'POST':
        form = AuthAdd(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['name'],
                # password=data['password']
            )
            Author.objects.create(
                user=u,
                name=data['name'],
                bio=data.get('bio')
            )

            return render(request, 'thanks.html')
    else:
        form = AuthAdd()

    return render(request, html, {'form': form})


def login_view(request):
    html = "login_form.html"

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                    )

    form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def edit_recipe_view(request, id):
    html = 'editrecipe.html'

    instance = RecipeItem.objects.get(id=id)


    if request.method == 'POST':
        edit_form = NewsAdd(
            request.POST,
            instance=instance
            )
        edit_form.save()

        return HttpResponseRedirect(reverse('homepage'))

    edit_form = NewsAdd(instance=instance)

    return render(request, html,
                  {'edit_form': edit_form, 'instance': instance})


def all_favorites(request):
    html = 'favorites.html'

    favorites = request.user.author.favorites.all()

    return render(request, html, {'favorites': favorites})


def add_favorite(request, id):

    favorite = RecipeItem.objects.get(id=id)

    request.user.author.favorites.add(favorite)

    return HttpResponseRedirect(reverse('allfavorites'))

