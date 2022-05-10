import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import os
import time
import random
import string


def randstr(n):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(n))


def create_table(cur, table_name, num_rows):
    cur.execute('DROP TABLE IF EXISTS %s' % table_name)
    cur.execute('CREATE TABLE %s (id INTEGER PRIMARY KEY)' % table_name)
    for i in range(num_rows):
        cur.execute('INSERT INTO %s VALUES (?)' % table_name, (i,))


class TestThread(threading.Thread):
    def __init__(self, db_name):
        super(TestThread, self).__init__()
        self.db_name = db_name
        self.conn = None

    def run(self):
        print('open')
        self.conn = sqlite3.connect(self.db_name)
        print('opened')
        cur = self
