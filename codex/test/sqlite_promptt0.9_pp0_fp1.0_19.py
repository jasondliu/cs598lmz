import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:../db/cve.db?mode=ro', uri=True)
from datetime import datetime
from hashlib import sha256
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, Comment
from pprint import pprint
from tqdm import tqdm
from os import path
from pathlib import Path
import unicodedata
import gzip
from scrapetime import *
#from scrape_sqlite import *

#================================================================================
# create_tb_cpe
#================================================================================
def create_tb_cpe():
    cn = sqlite3.connect(str(cfg['db']))
    cur = cn.cursor()

    sql = "CREATE TABLE IF NOT EXISTS cpe (id INTEGER PRIMARY KEY,part TEXT NOT NULL,vendor TEXT NOT NULL,product TEXT NOT NULL,version TEXT,update TEXT,edition TEXT,language TEXT)"
    cur.execute(sql)

