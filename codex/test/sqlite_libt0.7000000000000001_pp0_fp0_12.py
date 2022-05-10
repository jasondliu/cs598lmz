import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

# Variables
DB_FILE = "database.db"

# Setting up MySQLdb and loading the sqlite3 library
_sqlite_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# Injecting the MySQLdb into the sqlite3 library
_sqlite_lib.sqlite3_open.restype = ctypes.c_void_p
_sqlite_lib.sqlite3_open.argtypes = [ctypes.c_char_p]
_sqlite_lib.sqlite3_close.argtypes = [ctypes.c_void_p]
_sqlite_lib.sqlite3_prepare_v2.restype = ctypes.c_void_p
