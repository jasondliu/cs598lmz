import codecs
codecs.register_error('ignore', codecs.lookup('ignore'))

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.parse import quote
import time
import random
import os

# ダウンロード先ディレクトリ
download_dir = './img/'

# 各種設定
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36'
timeout = 5

# インスタンス
browser = Browser()
browser.set_handle_robots(False)

# リストにある画像をダウンロードする
def download_img(img_urls):
    for img_url in img_urls:
        try:
            # ファイ
