import codecs
codecs.register_error('strict', codecs.ignore_errors)
import requests
import re
import os
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count

# 创建文件夹
def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# 获取图片地址
def get_image_urls(page):
    image_urls = []
    url = 'https://www.meitulu.com/t/' + str(page)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    for img in soup.select('#main > div > div > p > a > img'):
        image_urls.append(img.get('src'))
    return image_urls

# 下载图片
def download_image(image
