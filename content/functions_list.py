import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
import requests
from .models import newsList
import re


def get_news_from_site(soup, url):
    news = None
    if 'habr.com' in url:
        news = soup.findAll("a", {"class": "post__title_link"})
        get_habr_news(news, url)
    if 'codeby.net' in url:
        news = soup.findAll("h2", {"class": "block-header"})
        get_codeby_news(news, url)

def get_habr_news(news, link):
    list_news = []
    for i in news:
        bd = newsList(site = link,
                      url = i.get_attribute_list('href')[0],
                      header= i.text,)
        bd.save()

def get_codeby_news(news, link):
    for i in news:
        print('hi nigga')
        temp = str(i.get_attribute_list)
        temp = temp.replace('>', ';')
        tmp = []
        line = ''
        for z in temp:
            line += z
            if z == ';':
                tmp.append(line)
                line = ''
        name = tmp[4]
        url = tmp[1]
        bd = newsList(site=link,
                      url= 'https://codeby.net' + url[10:-3],
                      header=name[1:-4], )
        bd.save()

def get_news(request,url):
    bd = newsList
    data = requests.get(url)
    page = data.text
    soup = BeautifulSoup(page, 'html.parser')


    get_news_from_site(soup,url)
