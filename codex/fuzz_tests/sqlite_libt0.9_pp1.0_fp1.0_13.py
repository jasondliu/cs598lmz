import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import glib

LOCALEDIR = os.path.join("share", "locale")
N_ = lambda x: x
BASE_ROW_EXISTS = '''
SELECT name FROM sqlite_master WHERE (type='table' or type='view') AND name=?;
'''
THREADSAFE = 1
ISOLATION_LEVEL_SERIALIZABLE = 4
COMPLETE = 0
COMPLETE_URI = 1
COMPLETE_FILESYSTEM_PATH = 2

BASE_VFS_NAME = 'gdbus-python-glib-example-%d'

_functions_lock = threading.Lock()
_base_functions_lock = threading.Lock()

_functions = None

_base_functions = None

_vfs_number = 0
_vfs_lock = threading.Lock()


def _load_sqlite_functions():
    global _functions
    _functions_lock.acquire()
    try:
        if _functions is None:
            _functions
