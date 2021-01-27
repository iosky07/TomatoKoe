from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('articles/', views.articles, name="articles"),
    path('articles/create/', views.form, name="form"),
    path('articles/update/<str:pk>/', views.updateArticle, name="update-article"),
    path('articles/delete/<str:pk_d>/', views.deleteArticle, name="delete-article"),
    path('articles/show/<str:pk>/', views.showArticle, name="show-article"),
    path('categories/delete/<str:pk>/', views.deleteCategory, name="delete-category"),
    path('categories/', views.categories, name="categories"),
    path('categories/create/', views.createCategory, name="create-category"),
]
