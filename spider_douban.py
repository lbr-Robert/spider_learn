#coding=utf8
#爬取豆瓣热门和最新电影列表

import requests
import re

def main(url,headers):
    data = requests.get(url,headers=headers).content

    #正则表达式匹配电影名称和评分
    pat_title = re.compile(r'"title":"(.*?)"')
    pat_rating = re.compile(r'"rate":"(.*?)"')
    pat_url = re.compile(r'"url":"(.*?)"')

    #提取电影名称和评分
    rate = pat_rating.findall(data)
    title = re.findall(pat_title, data)
    url_list = pat_url.findall(data)

    #将电影和评分合并到Toplist列表中
    Toplist=[]

    for i in range(0, len(rate)):
        TOP = title[i] + ":" + rate[i] + "  " + url_list[i].replace("\/","/")
        #逐条打印
        print TOP.decode('string_escape')

#定义参数
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

hot_url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=0"
new_url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=50&page_start=0"

for url in hot_url,new_url:
    main(url, headers)
    print("=================分割线=================")
