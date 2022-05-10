import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import MySQLdb
import re
import requests
import time
import json
from bs4 import BeautifulSoup
import datetime
import os
import threading


class CrawlWeibo(object):
    def __init__(self):
        self.__user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"  #"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        self.__cookie = {"Cookie": "_T_WM=a8f8b01babd0c84a78b9e8e8a215a9a2; SCF=Aq4Q2B
