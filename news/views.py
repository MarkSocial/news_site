from django.shortcuts import render, get_object_or_404

from news.models import News, Category
from django.http import Http404

# Create your views here.


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    news_item = get_object_or_404(News,pk=news_id)                                      #короткий вариант обработки исключений
    return render(request, 'news/view_news.html', {'news_item': news_item})

    # try:
    #     news_item = News.objects.get(pk=news_id)
    #     return render(request, 'news/view_news.html', {'news_item': news_item})       #второй вариант обработки исключений
    # except:
    #     raise Http404("No find news")