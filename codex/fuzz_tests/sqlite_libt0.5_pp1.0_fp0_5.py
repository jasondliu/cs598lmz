import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import signal
import sys

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from pysqlcipher import dbapi2 as sqlite

import sqlcipher
import sqlcipher.test

def get_lib(name):
    lib = ctypes.util.find_library(name)
    if not lib:
        raise Exception('Could not find ' + name)
    return ctypes.cdll.LoadLibrary(lib)

def create_db(path, key):
    db = sqlite.connect(path)
    db.execute('pragma key = "{}"'.format(key))
    db.execute('create table t1(a, b)')
    db.execute('insert into t1(a, b) values("one for the money", "two for the show")')
    db.commit()

def run_test(test, path, key):
    db = sqlite.connect(path)
    db.execute('pragma key = "{}"'.format(key))
