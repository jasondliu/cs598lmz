import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

from bs4 import BeautifulSoup
import requests
import csv
import os
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def get_urls(url):
    urls = []
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        urls.append(link.get('href'))
    return urls

def get_data(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
   
