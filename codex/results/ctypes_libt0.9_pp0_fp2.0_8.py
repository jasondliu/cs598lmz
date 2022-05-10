import ctypes
ctypes.CDLL('/usr/lib/libcrypto.so.10', mode=ctypes.RTLD_GLOBAL)
import MySQLdb
from requests import get
from bs4 import BeautifulSoup
import subprocess
import json
import datetime
from random import randint
import re
import sqlite3

db = MySQLdb.connect("localhost", "root", "12345678", "chromebook")
db.autocommit(True)
cursor = db.cursor()

KEYWORD = "湖北省武漢市新浪微博"

# path of the cache
PATH = "cache.sqlite3"
# title id in table "cache"
title_id = "title"
# content id in table "cache"
content_id = "content"
# url id in table "cache"
url_id = "url"

# year and month
year = "2020"
month = "01"

def init():
	"""
	init table: create table "cache"
	"""
	cursor.execute
