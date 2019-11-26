"""recipeBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipeBox import views
from recipeBox.models import Author, RecipeItem

admin.site.register(Author)
admin.site.register(RecipeItem)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('recipe/<int:key_id>/', views.recipe_item_view, name='itempage'),
    path('author/<int:key_id>/', views.author_view, name='authorpage'),
    path('news/', views.news_add),
    path('auth_Add/', views.auth_add, name='authaddpage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('editrecipe/<int:id>/', views.edit_recipe_view, name='editrecipe'),
    path('favorites/', views.all_favorites, name='allfavorites'),
    path('favorite/<int:id>/', views.add_favorite, name='favorite')
]
