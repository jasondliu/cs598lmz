import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import re
import json
import subprocess

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, CellStyle, Alignment
from openpyxl.styles.borders import Border, Side

# 歌单链接
playlist_url = 'http://qq.yh31.com/zjbd/dongman.html'
# 获取歌单的js脚本
get_playlist_js = r'var xhr = new XMLHttpRequest();xhr.open("get","PLAYLIST_URL",false);xhr.send(null);var r=xhr.responseText;r.replace(/[\r\n\t]/g, "");var s=r.match(/<ul class="index-list".*?>(.*?)<\/ul>/)[1];var reg=/<a class
