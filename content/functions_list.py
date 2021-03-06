import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
import requests
from .models import newsList
from .models import whiteList
import re

def check_name_len(name):
    if len(name)>55:
        return name[0:52] + '...'
    else:
        return name


def select_sites(site):
    b = whiteList(site=site)
    b.save()

def get_news_from_site(soup, url):
    news = None
    if 'habr.com/ru/top' in url:
        news = soup.findAll("a", {"class": "post__title_link"})
        get_habr_news(news, url)
    elif 'habr.com' in url:
        news = soup.findAll("a", {"class": "post__title_link"})
        get_habr_news(news, url)
    elif 'codeby.net' in url:
        news = soup.findAll("h2", {"class": "block-header"})
        get_codeby_news(news, url)
    elif 'xakep.ru/category/privacy/' in url:
        news = soup.findAll("h3", {"class": "entry-title"})
        get_xaker_news(news, url)

def get_habr_news(news, link):
    count = 0
    for i in news:
        if count == 5:
            break
        count += 1
        name = check_name_len(i.text)
        bd = newsList(site = link,
                      url = i.get_attribute_list('href')[0],
                      header = name,)
        bd.save()

def get_xaker_news(news, link):
    count = 0
    for i in news:
        if count == 5:
            break
        count += 1
        # print(i)
        temp = str(i.get_attribute_list)
        url = str(re.findall('https.*\/"', temp))[2:-3]
        header = str(re.findall('<span>.*<\/s', temp))[8:-5]
        name = check_name_len(header)
        bd = newsList(site = link,
                      url = url,
                      header = name,)
        bd.save()

def get_codeby_news(news, link):
    count = 0
    for i in news:
        if count == 5:
            break
        count += 1
        temp = str(i.get_attribute_list)
        temp = temp.replace('>', ';')
        tmp = []
        line = ''
        for z in temp:
            line += z
            if z == ';':
                tmp.append(line)
                line = ''
        name = check_name_len(tmp[4])
        url = tmp[1]
        bd = newsList(site=link,
                      url= 'https://codeby.net' + url[10:-3],
                      header=name[1:-4], )
        bd.save()

def get_news(request,url):
    check_site =  whiteList.objects.filter(site=url)
    if check_site:
        data = requests.get(url)
        page = data.text
        soup = BeautifulSoup(page, 'html.parser')


        get_news_from_site(soup,url)
