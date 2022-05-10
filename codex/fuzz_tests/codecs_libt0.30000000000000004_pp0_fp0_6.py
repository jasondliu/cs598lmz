import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 引入配置文件
from config import *

# 引入数据库模块
import pymysql

# 引入时间模块
import time

# 引入正则表达式模块
import re

# 引入爬虫模块
import requests

# 引入解析模块
from bs4 import BeautifulSoup

# 引入自定义模块
import common

# 引入系统模块
import sys

# 引入系统模块
import os

# 引
