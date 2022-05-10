import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db") if sqlite3.connect("123.db") fails

libc = ctypes.CDLL(ctypes.util.find_library("c"))
# For more information on gettid() and what it does, see the following URL:
# http://man7.org/linux/man-pages/man2/gettid.2.html
gettid = libc.syscall
libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"), mode=ctypes.RTLD_GLOBAL)
# For mode = RTLD_GLOBAL, see the following URL:
# http://lists.cs.uiuc.edu/pipermail/lldb-dev/2010-July/000257.html
# For the different modes of ctypes.CDLL(), see the following URL:
# https://docs.python.org/2/library/ctypes.html#ctypes.CDLL

libsqlite3.sqlite3_threadsafe.restype = ctypes.c_int
libsqlite3.sqlite3_open.
