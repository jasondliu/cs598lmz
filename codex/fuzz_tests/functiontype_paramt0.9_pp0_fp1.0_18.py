from types import FunctionType
list(FunctionType('exit'))
from  urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getLinks(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return []
    try:
        bsObj=BeautifulSoup(html.read(),'lxml')
        links=list(bsObj.findAll('a'))
    except AttributeError as e:
        return []
    return links
def getImage(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return []
    try:
        bsObj=BeautifulSoup(html.read(),'lxml')
        image=list(bsObj.findAll('src'))
    except AttributeError as e:
        return []
    return image


url='https://baike.baidu.com/item/Python/407313?fr=aladdin'
links=getLinks(url)
url
