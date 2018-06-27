#coding:utf-8
#python3.6

import sys

print(sys.version)
print(sys.path)

url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=538&kw=python&sm=0&sg=bfa5343e35474abeb0533325e048b588&p=1'

import requests
from bs4 import BeautifulSoup
headers = {
        'Referer': 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=538&kw=python&sm=0&sg=bfa5343e35474abeb0533325e048b588&p=1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
}

def urlfs(url):
    url_gather = []
    response = requests.get(url,headers = headers,timeout = 120)
    response.encoding = 'utf-8'
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    #print(soup)
    tds = soup('td',class_='zwmc')
    print(len(tds))
    for td in tds:
        try:
            a_g = td('a')[0]
            href_g = a_g['href']

            url_gather.append(href_g)

        except:
            continue
    return url_gather



# urlfs(url)
