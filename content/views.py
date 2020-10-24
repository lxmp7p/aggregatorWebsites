from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .functions_list import *
from .models import newsList

sites = ['HabrPython','HabrTop','Codeby','Xakep',]

habr_python = { 'name':'Хабр питон', 'url': 'https://habr.com/ru/hub/python/', }
habr_top = { 'name':'Хабр топ', 'url': 'https://habr.com/ru/top/', }
codeby = { 'name':'Codeby', 'url': 'https://codeby.net/', }
xakep = { 'name':'Xakep', 'url': 'https://xakep.ru/category/privacy/', }

def watch_content(request):
    newsList.objects.all().delete()
    url_list = [habr_python.get('url'),
                habr_top.get('url'),
                codeby.get('url'),
                xakep.get('url'),]
    for site in url_list:
        get_news(request, site)

    codebyList = newsList.objects.filter(site=codeby.get('url'))
    habrTopList = newsList.objects.filter(site=habr_top.get('url'))
    habrPyList = newsList.objects.filter(site=habr_python.get('url'))
    xakepPrivacyList = newsList.objects.filter(site=xakep.get('url'))
    return render(request, 'watchContentPage.html', {'codebyList': codebyList,
                                                     'habrTopList':habrTopList,
                                                     'habrPyList':habrPyList,
                                                     'xakerPrivacyList':xakepPrivacyList,
                                                    })

def open_options(request):
    print(request.POST)
    context = {'habr_python':'eqwqwwqe',
               'habr_top':habr_top,
               'codeby':codeby,
               'xakep':xakep,}

    return render(request, 'options.html', {'sites':sites})
