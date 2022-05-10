import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import subprocess
import sys

# class definition
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at:', time.ctime()
        self.res = apply(self.func, self.args)
        print self.name, 'finished at:', time.ctime()

# global variables
g_libc = ctypes.CDLL(ctypes.util.find_library('c'))
g_lock = threading.Lock()
g_db = sqlite3.connect('/tmp/test.db')
g_db.text_factory = str
g_db.execute('create table if not exists files (name text, size int)')
g_db.execute('create table if not exists dirs
