import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# coding = utf-8
import requests
import sys
# import csv
import os
import time
from datetime import date,datetime
import cx_Oracle
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class coin():
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.oracle_conn = cx_Oracle.connect('week_jhy/week_jhy@192.168.1.105/orcl')#orcl为数据库的SID
        self.cursor = self.oracle_conn.cursor()

    def download(self,coin_type):
        headers = {'Host': 'api.zb.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Ge
