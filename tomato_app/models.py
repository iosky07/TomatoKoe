from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=255)
    writter = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
