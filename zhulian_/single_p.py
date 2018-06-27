#coding:utf-8
#python3.6

import sys

#print(sys.version)
#print(sys.path)

url = 'http://jobs.zhaopin.com/CZ735252640J00137295301.htm'

import requests
from bs4 import BeautifulSoup
"""GET /CZ735252640J00137295301.htm HTTP/1.1
Host: jobs.zhaopin.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: adfbid=0; adfbid2=0; dywec=95841923; dywez=95841923.1529985098.1.1.dywecsr=other|dyweccn=121122523|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1529985098; _jzqc=1; _jzqy=1.1529985099.1529985099.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; _jzqckmp=1; __xsptplus30=30.1.1529985098.1529985098.1%231%7Cother%7Ccnt%7C121122523%7C%7C%23%23bIIuWlQn33nOoVQ8PE-Wwd6EjuR3Ohm7%23; __utmc=269921210; __utmz=269921210.1529985099.1.1.utmcsr=other|utmccn=121122523|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; JSSearchModel=0; LastCity%5Fid=538; LastCity=%e4%b8%8a%e6%b5%b7; dywea=95841923.761462519001611100.1529985098.1529985098.1529994237.2; __utma=269921210.1668810966.1529985099.1529985099.1529994237.2; _jzqa=1.3820833362502965000.1529985099.1529985099.1529994237.2; LastSearchHistory=%7b%22Id%22%3a%220e064097-ccd6-43e4-ac36-16770ba1cfef%22%2c%22Name%22%3a%22python+%2b+%e4%b8%8a%e6%b5%b7%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d538%26kw%3dpython%26sm%3d0%26sg%3dbfa5343e35474abeb0533325e048b588%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1529994252079%2b0800)%5c%2f%22%7d; _jzqb=1.2.10.1529994237.1; dyweb=95841923.8.10.1529994237; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1529995660; __utmt=1; __utmb=269921210.8.10.1529994237; referrerUrl=; stayTimeCookie=1529995659742
"""


headers = {
    'Host': 'jobs.zhaopin.com',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cookie':'adfbid=0; adfbid2=0; dywec=95841923; dywez=95841923.1529985098.1.1.dywecsr=other|dyweccn=121122523|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1529985098; _jzqc=1; _jzqy=1.1529985099.1529985099.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; _jzqckmp=1; __xsptplus30=30.1.1529985098.1529985098.1%231%7Cother%7Ccnt%7C121122523%7C%7C%23%23bIIuWlQn33nOoVQ8PE-Wwd6EjuR3Ohm7%23; __utmc=269921210; __utmz=269921210.1529985099.1.1.utmcsr=other|utmccn=121122523|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; JSSearchModel=0; LastCity%5Fid=538; LastCity=%e4%b8%8a%e6%b5%b7; dywea=95841923.761462519001611100.1529985098.1529985098.1529994237.2; __utma=269921210.1668810966.1529985099.1529985099.1529994237.2; _jzqa=1.3820833362502965000.1529985099.1529985099.1529994237.2; LastSearchHistory=%7b%22Id%22%3a%220e064097-ccd6-43e4-ac36-16770ba1cfef%22%2c%22Name%22%3a%22python+%2b+%e4%b8%8a%e6%b5%b7%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d538%26kw%3dpython%26sm%3d0%26sg%3dbfa5343e35474abeb0533325e048b588%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1529994252079%2b0800)%5c%2f%22%7d; _jzqb=1.2.10.1529994237.1; dyweb=95841923.8.10.1529994237; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1529995660; __utmt=1; __utmb=269921210.8.10.1529994237; referrerUrl=; stayTimeCookie=1529995659742'

}




def soup_g(url):
    url_gather = []
    response = requests.get(url,headers = headers,timeout = 120)
    response.encoding = 'utf-8'
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    return soup





import pandas as pd
import numpy as np
import re
def soup_excel(soup):


    try:

        job = soup.body.h1.string
    except:
        job = soup.head.title.string
    job = str(job)
    #print(job)
    #print(type(job))

    tag0s = soup('ul',class_='terminal-ul')
    tag0s = str(tag0s)
    tag0s = re.sub('<.+?>','',tag0s)
    print(tag0s)



    def zz_r(word):
        p = word + '：(.+)'
        pattern = re.compile(p)

        try:
            gt = re.findall(pattern,tag0s)[0]

        except:
            gt = 'null'
        return gt


    #list = ['web','job','职位月薪','工作地点','工作性质','工作经验','最低学历','职位类别','公司规模','公司地址']

    list_g = [url,job,zz_r('职位月薪'),zz_r('工作地点'),zz_r('工作性质'),zz_r('工作经验'),zz_r('最低学历'),zz_r('职位类别'),zz_r('公司规模'),zz_r('公司地址')]

    if 'python' in job:

        return list_g
    else:
        return []


soup = soup_g(url)
list0 = soup_excel(soup)

#print(soup)
# print(list0)



