import ctypes
import ctypes.util
import threading
import sqlite3
import json
import sys
import os
import time

# The following is a workaround for a bug in sqlite3.
# See http://stackoverflow.com/questions/12881294/sqlite3-programmingerror-you-must-not-use-8-bit-bytestrings-unless-you-use-a-te
if sys.version_info[0] < 3:
    import codecs
    def unicode_to_bytes(s):
        return codecs.utf_8_encode(s)[0]
else:
    def unicode_to_bytes(s):
        return s.encode('utf-8')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class SQLiteWrapper(object):
    def __init__(self, filename):
        self.filename = filename
        self.conn = None
        self.cursor = None
        self.lock =
