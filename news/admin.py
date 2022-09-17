from django.contrib import admin
from news.models import Category, News

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'category', 'created_at',
                    'updated_at', 'is_published' ]
    list_display_links = ['title']
    list_filter = ['category']
    search_fields = ['is_published']
    list_editable = ['is_published']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']