import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import time

libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))


def c_str(string):
    return ctypes.c_char_p(string.encode('utf-8'))


def c_str_array(strings):
    return (ctypes.c_char_p * len(strings))(*map(c_str, strings))


class Sqlite3Thread(threading.Thread):
    def __init__(self, path):
        super(Sqlite3Thread, self).__init__()
        self.path = path
        self.conn = None
        self.cursor = None
        self.ret = None
        self.is_run = True

    def run(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT)')
