from django.shortcuts import render
from django.shortcuts import get_object_or_404

from news.models import News


def news_list(request):
    """Список статей"""
    news = News.objects.all()
    context = {"news": news}
    return render(request, "news/news_list.html", context)


def new_single(request, pk):
    """Статья"""
    new = get_object_or_404(News, id=pk)
    context = {"new": new}
    return render(request, "news/new_single.html", context)