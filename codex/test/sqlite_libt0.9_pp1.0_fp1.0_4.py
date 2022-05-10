import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time

class tdb(object):

    def __init__(self, path):
        self.__lock = threading.RLock()
        self.__handle = tdb.__open_db(path)
        assert self.__handle, 'Could not open database: %s' % path
        
    def __enter__(self):
        return self.__lock.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.__lock.__exit__(exc_type, exc_val, exc_tb)
    
    def __iter__(self):
        cursor = tdb.cursor(self.__handle)
        try:
            cursor.iternext()
            return cursor
        except:
            cursor.close()
            return
            
