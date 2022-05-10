import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import requests
from bs4 import BeautifulSoup as BS
import sys

'''
    author: snowwhite
    date: 2019-02-25
    从百度贴吧中抓取小说，并保存到本地
    要知道的贴吧名称，去百度搜索书名
'''

def getPage(url):
    try: 
            r = requests.get(url, timeout = 30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
    except:
        return ""

def getPageNum(content):
    #获取帖子页面总数
    soup = BS(content, 'lxml')

