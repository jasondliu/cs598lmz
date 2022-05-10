import threading
threading.stack_size(8192*4)

from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import os

# 저장 경로
save_path = 'D:/stock/'

def get_url(url):
    response = urlopen(url)
    return response.read()

def get_soup(url):
    soup_data = BeautifulSoup(get_url(url), "html.parser")
    return soup_data

def get_stock_code_name(soup):
    stock_code_name = []
    for idx, item in enumerate(soup.find_all('tr')):
        if idx == 0:
            continue
        item_list = item.find_all('td')
        stock_code = item_list[0].text
        stock_name = item_list[1].text
        stock_code_name.append([stock_code, stock_name])
    return stock_code
