import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import re
import codecs

try:
    import lxml.etree as ET
except:
    import xml.etree.cElementTree as ET


class GoogleSpell(object):
    def __init__(self, dict_path):
        self.dict_path = dict_path
        self.conn = sqlite3.connect(self.dict_path)
        self.lock = threading.Lock()

    def check(self, word):
        with self.lock:
            c = self.conn.cursor()
            c.execute('select sum(cnt) from words where word=?',
                      (word, ))
            r = c.fetchone()[0]
            if r > 0:
                return True
            return False

    def suggest(self, word, max_sugg=10):
        with self.lock:
            c = self.conn.cursor()
            c.execute('select word from words where word like ? '
                      'order by cnt desc limit ?', (word + '%', max_sugg, ))

