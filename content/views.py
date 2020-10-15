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
                'https://habr.com/ru/top/',
                'https://xakep.ru/category/privacy/',]
    for site in url_list:
        get_news(request, site)

    codebyList = newsList.objects.filter(site='https://codeby.net/')
    habrTopList = newsList.objects.filter(site='https://habr.com/ru/top/')
    habrPyList = newsList.objects.filter(site='https://habr.com/ru/hub/python/')
    xakerPrivacyList = newsList.objects.filter(site='https://xakep.ru/category/privacy/')
    return render(request, 'watchContentPage.html', {'codebyList': codebyList,
                                                     'habrTopList':habrTopList,
                                                     'habrPyList':habrPyList,
                                                     'xakerPrivacyList':xakerPrivacyList,
                                                    })

