import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect().
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute('SELECT SQLITE_VERSION()')
print "Sqlite3 version:", cur.fetchone()[0]
# The sqlite3 library does not explicitly link to libdl or libpthread.
# But we need to make sure the shared library is compiled with
# -lpthread so the connection can be shared between threads.
# At least on Linux, the sqlite3 library is compiled with -lpthread.
# But this is not the case on FreeBSD.
# In any case, we explicitly try to load the library with ctypes.
# This is a simple way to check that it is linked correctly.
libdl = ctypes.CDLL(ctypes.util.find_library("dl"))
libpthread = ctypes.CDLL(ctypes.util.find_library("pthread"))
# Test sqlite3.connect() with threads.
# The sqlite3 library is thread-safe, but each connection can only be used
# in a single thread.
# We need a lock to ensure that each connection
