from django.shortcuts import render
from .utils import *
from .secrets import API_KEY

# Create your views here.
def home(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-11-30&sortBy=publishedAt&apiKey=a47e7903f2984016880269ddbbf4ed70'
    get_news_from_api(url)
    return render(request, 'home.html')