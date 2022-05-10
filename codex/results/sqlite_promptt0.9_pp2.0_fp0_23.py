import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(). Also make sure that select access to sqlite3 works.
for filename in [':memory:', 'testcase.db', 'testcase.db3', 'testcase.sqlite']:
    conn = sqlite3.connect(filename)
    try:
        conn.cursor().execute('select 3').fetchall()
    finally:
        conn.close()
# Test to verify the timeout= argument takes effect.
count = []
conn = sqlite3.connect(':memory:', timeout=0.1)
import time
start = time.time()
with conn.cursor():
    pass
end = time.time()
conn.close()
assert 0.09 < end - start < 0.12
conn = sqlite3.connect(':memory:', timeout=.1)
# Test the APSW module
import ctypes
import ctypes.util
_apsw = ctypes.CDLL(ctypes.util.find_library('apsw'))
_apsw.sqlite3_threadsafe.restype = ctypes.c_int
threading = _apsw.sqlite
