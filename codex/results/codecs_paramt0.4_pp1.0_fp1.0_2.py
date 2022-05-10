import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

from datetime import datetime
import os
import re
import sys
import time
from urllib.parse import quote
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

from app.models import db, Movie


def get_movie_info(url, year=None):
    """
    获取电影详情页面信息

    :param url: 电影详情页面URL
    :param year: 电影年份
    :return: 电影详情信息
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
