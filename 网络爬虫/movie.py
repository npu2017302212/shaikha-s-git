# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:34:35 2020

@author:
"""

from bs4 import BeautifulSoup
import re
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }
txt = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled/movie.txt', 'a', encoding = 'utf-8')

def main(pages):
    url = 'https://movie.douban.com/top250?start=' + str(25 * i)
    html = RequestData(url)
    r = requests.get(url, headers = headers, timeout = 10)
    soup = BeautifulSoup(r.text, "lxml")
    lists = soup.find_all('div', class_ ='item')
    for each in lists:
        movie = {}
        name = each.find('div', class_ ='hd').a.span.text.strip()
        movie['电影名'] = name
        ranking = each.find('div', class_ ='pic').em.text.strip()
        movie['排名'] = ranking
        temp = each.find('div', class_ ='bd')
        temp = temp.find('p', class_='').text.strip()
        temp = temp.replace('\n', "")
        temp = temp.replace(" ", "")
        temp = temp.replace("\xa0", "")
        director = re.findall(r'[导演:].+[主演:]', temp)[0]
        director = director[3:len(director) - 3]
        movie['导演'] = director
        release_date = re.findall(r'[0-9]{4}', temp)[0]
        movie['上映日期'] = release_date
        region = re.findall(r'[0-9]*[/].+[/]', temp)[0]
        region = region[1:]
        region = region[region.index('/') + 1:]
        region = region[:-1]
        movie['制片国家/地区'] = region
        star = each.find('div', class_ ='star')
        star = star.find('span', class_ ='rating_num').text.strip()
        movie['评分'] = star
        detail = each.find('p', class_ ='quote')
        detail = detail.find('span', class_ ='inq').text.strip()
        movie['详情'] = detail
        print(movie)
        print(movie, file = txt)

def RequestData(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.test
    return None

if __name__ == '__main__':
    for i in range(0,2):
        main(i)
