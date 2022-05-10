import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect to ensure we have sqlite3 module
try:
    from sqlite3 import OperationalError
except ImportError:
    class OperationalError(Exception): pass

# Py3k compatibility kludge
try:
    unicode
except NameError:
    basestring = unicode = str

try:
    # Only in Python 3.2
    from functools import lru_cache
except ImportError:
    def lru_cache(maxsize=128):
        def decorating_function(user_function):
            cache = {}
            sentinel = object()
            def wrapper(*args):
                res = cache.get(args, sentinel)
                if res is not sentinel:
                    return res
                res = user_function(*args)
                cache[args] = res
                return res
            return wrapper
        return decorating_function

from logbook import Logger
log = Logger("file_manager")

