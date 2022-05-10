import ctypes
import ctypes.util
import threading
import sqlite3

def _ensure_bytes(s):
    if isinstance(s, bytes):
        return s
    else:
        return s.encode('utf-8')

def _ensure_unicode(s):
    if isinstance(s, str):
        return s
    else:
        return s.decode('utf-8')

class MDBL(object):
    __libname = ctypes.util.find_library("mdbl")
    __lib = ctypes.CDLL(__libname)

    def __init__(self, path, create_table=False):
        self.__mdbl = jmdbl.MDBL(path, create_table)
        self.__conn = sqlite3.connect(':memory:')
        self.__cursor = self.__conn.cursor()
        self.__max_key_len = self.__mdbl.get_max_key_len()
        self.__max_value_len = self.__mdbl.get_max_value_len()
        self.__key_index =
