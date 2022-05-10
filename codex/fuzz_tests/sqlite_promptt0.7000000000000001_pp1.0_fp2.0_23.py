import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# https://www.sqlite.org/threadsafe.html
# 1 - Single-thread.
# 2 - Serialized.
# 3 - Multi-thread, default.

ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True).pthread_create.restype = ctypes.c_int

def _check_open_args(filename, flags, detect_types, isolation_level,
                     check_same_thread, uri, factory=None):
    if check_same_thread and (flags & 0o2000000):
        raise ValueError("check_same_thread cannot be enabled while using "
                         "the multithreaded sqlite3 library")
    if detect_types:
        raise ValueError("the detect_types parameter is not supported "
                         "when using the sqlite3 library")
    if factory:
        raise ValueError("the factory parameter is not supported "
                         "when using the sqlite3 library")
    if uri:
        raise ValueError("URI connections are not supported "
                         "when using the sqlite3
