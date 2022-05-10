import ctypes
import ctypes.util
import threading
import sqlite3
import re
import os
import sys
import time
import shutil
import string
import sippy
import sippy.Time.Time

(VERBOSE, WARNING, ERROR, NONE) = (255, 128, 64, 1)

class SipConf(object):
    def __init__(self, cf_name, defaults = True, cf_defaults = None):
        self.name = cf_name
        self.locker = threading.RLock()
        self.local_config = {}
        self.db_config = {}
        self.parent = None
        self.base_config = cf_defaults
        if defaults:
            self.connect_db()
            self.load(self.db_config, cf_name)

    def connect_db(self):
        self.conn = sqlite3.connect(self.name)
        self.cur = self.conn.cursor()

    def load(self, data_dict, table_name):
        self.cur.execute("select attr, val from %s" % table_name)
        res =
