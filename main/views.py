from unicodedata import category
from django.shortcuts import render
from .models import News, Category
from appvid.models import Video
# Create your views here.


def index(request):
    vid = Video.objects.all().order_by('-id')
    # first_news = News.objects.first()
    first_news = News.objects.last()
    # three_news = News.objects.all()[1:5]
    three_news = News.objects.all().order_by('-id')[1:4]
    #[1:5]
    three_categories = Category.objects.all()[0:3]
    return render(request, 'index.html', {
        'first_news': first_news,
        'three_news': three_news,
        'three_categories': three_categories,
        'vid': vid,

    })

def all_news(request):
    all_news = News.objects.all().order_by('-id')
    return render(request, 'all-news.html', {'all_news': all_news})


def detail(request, id):
    news = News.objects.get(pk=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    return render(request, 'detail.html', {
        'news': news,
        'related_news': rel_news
    })
# fetch all category
def all_category(request):
    cats = Category.objects.all().order_by('-id')
    return render(request, 'category.html', {
        'cats': cats,
    })


def category(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'all_news': news,
        'category': category,
    })
