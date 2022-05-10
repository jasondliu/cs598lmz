import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import time

#from ctypes import *
from ctypes.util import find_library
from ctypes import cdll
from ctypes import c_int
from ctypes import c_char_p
from ctypes import c_char
from ctypes import c_void_p
from ctypes import c_size_t
from ctypes import c_uint
from ctypes import Structure
from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import byref

from ctypes.util import find_library
libc = cdll.LoadLibrary(find_library("c"))

class sqlite3(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = None
        self.stmt = None
        self.sqlite = cdll.LoadLibrary(find_library("sqlite3"))
        self.sqlite.sqlite3_open.argtypes = [c_char_p, POINTER(c_void_p)]
        self.sqlite.sqlite3
