import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect ?
from pysqlite2 import dbapi2 as sqlite3
from string import rstrip

db_mutex = threading.Lock()

DEEPSEE_EXPOSED = ctypes.c_int.in_dll(ctypes.windll.curses, 'DEEPSEE_EXPOSED').value

def _thread_decorator(f):
    def wrapper(*args, **kwargs):
        global db_mutex
        db_mutex.acquire()
        try:
            retval = f(*args, **kwargs)
        except:
            db_mutex.release()
            raise
        db_mutex.release()
        return retval
    return wrapper

class DeepSeePerson(object):
    """DeepSeePerson
    Class representing a data record listing a name and score.

    """
    def __init__(self, name = '', score = -1):
        self._name = name
        self._score = score

