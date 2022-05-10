import ctypes
import ctypes.util
import threading
import sqlite3
import sqlite3.dbapi2 as sqlitedb
import os
import weakref
import sys
import re
import datetime

def utf8(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return str(s)

def native_string(s):
    if not isinstance(s, unicode):
        return s
    try:
        return s.encode(sys.getfilesystemencoding())
    except UnicodeEncodeError:
        return s.encode('utf8')

def to_unicode(s):
    if isinstance(s, unicode):
        return s
    try:
        s = s.decode('utf8', 'ignore')
    except UnicodeDecodeError:
        s = s.decode(sys.getfilesystemencoding(), 'ignore')
    return s

class ThreadSafeList(list):
    '''A thread safe list'''
    def __init__(self):
        self.lock = threading.Lock()
        super(ThreadSafeList
