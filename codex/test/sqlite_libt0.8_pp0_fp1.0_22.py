import ctypes
import ctypes.util
import threading
import sqlite3
from time import sleep
from collections import OrderedDict
from multiprocessing import Process, Lock, Manager

from storage import storage
import json
import os

_libdevguide = None
_db_path = os.path.join(os.path.dirname(__file__), '..', '..', '_build',
        'libdevguide-db.so')

def _init_libdevguide():
    """
    Initialize libdevguide
    """
    global _libdevguide
    if not _libdevguide:
        libdevguide = ctypes.cdll.LoadLibrary(_db_path)
        libdevguide.init_DB.restype = ctypes.c_void_p
        libdevguide.get_DB_entries.restype = ctypes.c_int
        libdevguide.get_DB_entries.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
        libdevguide.get_DB_values.restype = ctypes.c_int
       
