import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import binascii
import platform
import socket
import select
import signal
import sys
import time

VERSION = '0.8.2'

# On OS X, a number of bugs in the built-in sqlite3 library
# cause it to segfault. So we'll try to use the system library,
# and if that fails, we'll just use the built-in.
sqlite3_path = ctypes.util.find_library('sqlite3')
if sqlite3_path:
    ctypes.cdll.LoadLibrary(sqlite3_path)
SQLITE_OK = 0
SQLITE_ROW = 100

if 'linux' in sys.platform:
    try:
        import systemd.daemon
    except ImportError:
        class systemd:
            @staticmethod
            def notify(what):
                pass
else:
    class systemd:
        @staticmethod
        def notify(what):
            pass

# If a set of cached results is older than this, don't
# use it.
CACHE_TTL
