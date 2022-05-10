import codecs
codecs.register_error('strict', codecs.ignore_errors)

import json
import re
import requests

from bs4 import BeautifulSoup

from . import models


def parse_html(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf8'
    except requests.exceptions.ConnectionError as e:
        print(e)
        raise
    return BeautifulSoup(r.text, 'lxml')


def parse_string(string):
    return BeautifulSoup(string, 'lxml')


def extract_items(url):
    soup = parse_html(url)
    items = soup.select('div.item')

    for item in items:
        href = item.select_one('a').get('href')
        title = item.select_one('a').get_text()
        title = title.strip('\n')
        title = re.sub('\s+', '', title)
        if title == '':
            continue
        image_url = item.select_one('img').get('src')

