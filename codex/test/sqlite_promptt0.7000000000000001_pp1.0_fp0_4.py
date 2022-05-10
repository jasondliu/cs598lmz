import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared", uri=True)

# import ctypes.wintypes

# def dllfunc(rettype, name, *args):
#     args = tuple(ctypes.c_void_p if x == 'void*' else x for x in args)
#     return ctypes.WINFUNCTYPE(rettype, *args)((name, ctypes.cdll.LoadLibrary('sqlite3')))

# sqlite3_key = dllfunc(ctypes.c_int, 'sqlite3_key', 'void*', 'char*', 'int')
# sqlite3_rekey = dllfunc(ctypes.c_int, 'sqlite3_rekey', 'void*', 'char*', 'int')

# sqlite3_open = dllfunc(ctypes.c_int, 'sqlite3_open', 'char*', 'void**')
# sqlite3_exec = dllfunc(ctypes.c_int, 'sqlite3_exec', 'void*', 'char*', 'void*
