import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 使用正则表达式进行模糊匹配
import re

# 引入爬虫框架
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request

# 引入爬虫项目配置
from scrapy.utils.project import get_project_settings

# 引入容器
from collections import OrderedDict

# 引入数据库模块
import pymysql
from twisted.enterprise import adbapi

# 引入时间模块
import time
import datetime

# 设置编码
import sys
reload
