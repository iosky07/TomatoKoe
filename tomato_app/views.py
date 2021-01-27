from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import ArticleForm, CategoryForm
from pprint import pprint

# Create your views here.
def form(request, template_name='form/form.html', form_class=ArticleForm):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            if form_class == ArticleForm:
                return redirect('articles')
            elif form_class == CategoryForm:
                return redirect('categories')
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def home(request):
    articles = Article.objects.all()

    context = {'articles' : articles}
    return render(request, 'home.html', context)

def articles(request):
    articles = Article.objects.all()
    return render(request, 'pages/article/index.html', {'articles' : articles})

def updateArticle(request, pk):
    update = Article.objects.get(id=pk)
    form = ArticleForm(instance=update)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=update)

        if form.is_valid():
            form.save()
            return redirect('articles')

    return render(request, 'form/form.html', {'form': form})

def deleteArticle(request, pk_d):
    delete = Article.objects.get(id=pk_d)
    data = Article.objects.all()

    for da in data:
        data = da.title

    if request.method == 'POST':
            delete.delete()
            return redirect('/articles')

    context = {
        'delete': delete,
        'data' : data
    }
    return render(request, 'pages/article/delete.html', context)

def categories(request):
    categories = Category.objects.all()
    return render(request, 'pages/category/index.html', {'categories' : categories})

def createCategory(request):
    return form(request, template_name='form/form.html', form_class=CategoryForm)

def deleteCategory(request, pk):
    delete = Category.objects.get(id=pk)
    data = Category.objects.filter(id=pk)

    for d in data:
        data = d.category

    if request.method == 'POST':
            delete.delete()
            return redirect('/categories')

    context = {
        'delete': delete,
        'data' : data
    }
    return render(request, 'pages/category/delete.html', context)


def showArticle(request, pk):
    data = Article.objects.filter(id=pk)

    context = {
        'data': data
    }
    return render(request, 'pages/article/show.html', context)

