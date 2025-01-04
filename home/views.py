from django.shortcuts import render
from .utils import *
import requests

# Create your views here.
def home(request):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'finance',
        'from': '2024-12-23',
        'sortBy': 'popularity',
        'apiKey': 'a47e7903f2984016880269ddbbf4ed70',  # Replace with your actual API key.
        'pageSize': 20
    }
    
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return render(request, 'home.html', context = {'articles' : articles})