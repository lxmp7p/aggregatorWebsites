from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .functions_list import *
from .models import newsList
def watch_content(request):
    newsList.objects.all().delete()
    url_list = ['https://habr.com/ru/hub/python/',
                'https://codeby.net/',
                'https://habr.com/ru/top/',]
    for site in url_list:
        get_news(request, site)

    codebyList = newsList.objects.filter(site='https://codeby.net/')[:5]
    habrTopList = newsList.objects.filter(site='https://habr.com/ru/top/')[:5]
    habrPyList = newsList.objects.filter(site='https://habr.com/ru/hub/python/')[:5]
    return render(request, 'watchContentPage.html', {'codebyList': codebyList, 'habrTopList':habrTopList, 'habrPyList':habrPyList })

