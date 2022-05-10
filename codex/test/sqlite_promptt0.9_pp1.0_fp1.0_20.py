import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection object
#   https://www.python.org/dev/peps/pep-0249/#connection-objects

# Python threads:
#   http://www.voidspace.org.uk/python/articles/threading.shtml

POSIX = 'posix' in sys.builtin_module_names
if POSIX:
    from ctypes.util import find_library
else:
    _osx_support = ('libSystem' in ctypes.util.find_library('c'))

    def find_library(name):
        if name in ('readline', 'termcap'):
            return name


libc = ctypes.CDLL(find_library('c'))
if libc.FAKE_LIBC:
    libsqlite = ctypes.CDLL('sqlite3', use_errno=True)
else:
    libsqlite = ctypes.CDLL(find_library('sqlite3'), use_errno=True)
