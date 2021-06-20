from django.contrib import admin
from .models import Article
 
# Register your models here.
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
   list_filter = ('title', 'description')          # add your filters
   list_display = ('title', 'description')