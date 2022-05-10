import ctypes
import ctypes.util
import threading
import sqlite3
import struct
import sys
import traceback
import os

posix = (sys.platform != 'win32')

try:
    from pylib.py2 import xrange
except ImportError:
    xrange = range

try:
    int_types = (int, long)
except NameError:
    int_types = (int,)

def debug(str):
    sys.stderr.write('%s\n' % str)

def open_database(path):
    while True:
        try:
            return sqlite3.connect(path)
        except sqlite3.OperationalError:
            time.sleep(0.1)

def bytes_to_long(data):
    res = 0
    for x in data:
        res <<= 8
        res += ord(x)
    return res

def long_to_bytes(l):
    res = bytearray()
    while l:
        res.append(l & 0xff)
        l >>= 8
