import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re

try:
    from . import _lib
except ImportError:
    _lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.RTLD_GLOBAL)

_thread = threading.Thread()
_thread.daemon = True
_thread_lock = threading.Lock()
_thread_lock.acquire()
_thread.start()
_thread_lock.release()

_pending_requests = []
_pending_requests_lock = threading.Lock()
_pending_requests_lock.acquire()

# SQLite's threading mode is serialized.  We don't want to be
# serialized, so we need to make sure that there is only one thread
# executing SQLite at any given time.  We do this by wrapping calls to
# SQLite in a thread lock.  We can't just use the lock to serialize
# everything, though, because certain SQLite calls (specifically
# sqlite3_prepare_v2 and sqlite3_finalize) need
