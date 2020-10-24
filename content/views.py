from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .functions_list import *
from .models import newsList
from .models import whiteList


sites = [{ 'name':'HabrPython', 'url': 'https://habr.com/ru/hub/python/', },
         { 'name':'HabrTop', 'url': 'https://habr.com/ru/top/', },
         { 'name':'Codeby', 'url': 'https://codeby.net/', },
         { 'name':'Xakep', 'url': 'https://xakep.ru/category/privacy/', }]


def watch_content(request):
    newsList.objects.all().delete()
    url_list = []
    for site in sites:
        url_list.append(site.get('url'))
    for site in url_list:
        get_news(request, site)

    habrPyList = newsList.objects.filter(site=sites[0].get('url'))
    habrTopList = newsList.objects.filter(site=sites[1].get('url'))
    codebyList = newsList.objects.filter(site=sites[2].get('url'))
    xakepPrivacyList = newsList.objects.filter(site=sites[3].get('url'))
    print(codebyList)
    print(habrPyList)
    print(habrTopList)
    print(xakepPrivacyList)
    return render(request, 'watchContentPage.html', {'codebyList': codebyList,
                                                     'habrTopList':habrTopList,
                                                     'habrPyList':habrPyList,
                                                     'xakerPrivacyList':xakepPrivacyList,
                                                    })

def open_options(request):
    if request.POST:
        siteList = []
        siteName = ''
        for i in request.POST.get('site'):
            if i != ',':
                siteName += i
            else:
                siteList.append(siteName)
                siteName = ''
        accept_urls = []
        whiteList.objects.all().delete()
        for i in siteList:
            for site in sites:
                if i == site.get('name'):
                    select_sites(site.get('url'))

    url_list = []
    for site in sites:
        url_list.append(site.get('name'))

    return render(request, 'options.html', {'sites':url_list})
