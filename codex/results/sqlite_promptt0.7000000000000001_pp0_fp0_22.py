import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import time
import random
import os

SQLITE_SO = ctypes.util.find_library('sqlite3')
if not SQLITE_SO:
    raise Exception("Can't find sqlite3 library")

def lookup_symbol(lib, name):
    symbolPointer = lib.__getattr__(name)
    if not symbolPointer:
        return None
    return symbolPointer.value

#: Pointer to sqlite3_initialize()
sqlite3_initialize = ctypes.CFUNCTYPE(ctypes.c_int)(
    lookup_symbol(ctypes, 'sqlite3_initialize')
)
#: Pointer to sqlite3_shutdown()
sqlite3_shutdown = ctypes.CFUNCTYPE(ctypes.c_int)(
    lookup_symbol(ctypes, 'sqlite3_shutdown')
)
#: Pointer to sqlite3_open()
sqlite3_open = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.
