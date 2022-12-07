from django.contrib import admin
from .models import *

# admin.site.register((Post,TopPost))
  
@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date', 'tanlov')


@admin.register(TopPost)
class ArticleTopPost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date', 'tanlov')

@admin.register(Admin)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'content')