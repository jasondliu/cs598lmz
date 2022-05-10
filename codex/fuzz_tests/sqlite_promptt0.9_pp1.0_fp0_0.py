import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# https://docs.python.org/2/library/ctypes.html
# https://www.sqlite.org/c3ref/intro.html
# https://www.sqlite.org/c3ref/constlist.html
# https://www.sqlite.org/c3ref/column_blob.html
# https://www.sqlite.org/c3ref/exec.html
# http://svn.python.org/projects/python/trunk/Modules/_ctypes/callproc.c
# http://stackoverflow.com/questions/13814847/retrieving-column-data-from-sqlite3-using-python

class Connection:
    def __init__(self, db=None):
        self.db = db
        self.sqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
        if self.sqlite3 == None:
            raise ImportError('Could not find libsqlite3')
        self.sqlite3.sqlite3_
