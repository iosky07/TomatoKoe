from django.forms import ModelForm
from django import forms
from .models import *

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'