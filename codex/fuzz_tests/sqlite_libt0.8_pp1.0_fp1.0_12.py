import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import stat
import fnmatch

# detect platform
try:
  osTmp = os.uname()
  osPlatform = osTmp.sysname
except:
  osPlatform = sys.platform

# detect sqlite3 lib
if osPlatform == "posix":
  from ctypes.util import find_library
  sqlite3lib = find_library('sqlite3')
  if sqlite3lib is None:
    sqlite3lib = 'libsqlite3.so.0'
elif osPlatform == "win32":
  sqlite3lib = 'sqlite3.dll'

libsqlite3 = ctypes.CDLL(sqlite3lib)

# define sqlite3 structures
_sqlite3_stmt = ctypes.c_void_p
_sqlite3 = ctypes.c_void_p

sqlite3_stmt_ptr = ctypes.POINTER(_sqlite3_stmt)
sqlite3_ptr = ctypes.POINTER(_sqlite3)

# define sqlite
