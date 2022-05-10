import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import sys, os
import logging
import itertools as it

if sys.version_info < (3, ):
    range = xrange

#
# Define the SQLite library interface
#
_lib = ctypes.util.find_library('sqlite3')
_lib = ctypes.CDLL(_lib)
_sqlite_api = {
    'create_function': (
        'sqlite3_create_function',
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int,
         ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p),
        ctypes.c_int,
    ),
    'column_count': (
        'sqlite3_column_count',
        (ctypes.c_void_p,),
        ctypes.c_int,
    ),
    'column_type': (
        'sqlite3_column_
