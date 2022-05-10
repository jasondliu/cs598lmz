import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")
conn.close()
# Test sqlite3.Cursor
cursor = conn.cursor()
cursor.close()
del cursor
# Test sqlite3.Row
row = cursor.fetchone()
del row
# Thread support for sqlite3
assert sqlite3.threadsafety >= 2, sqlite3.threadsafety
# Test sqlite3.connections
connections = set([])
def generator():
    for i in range(10000):
        connections.add(sqlite3.connect(":memory:"))
        yield None
    while connections:
        connections.pop().close()
thread = threading.Thread(target=generator().next)
thread.start()
thread.join()
# Test importing internal sqlite3 module
from sqlite3 import _sqlite3
# Test internal _sqlite3 calls
ctypes.CDLL(ctypes.util.find_library('sqlite3'), _sqlite3.SQLITE_API)
_sqlite3.complete_statement(b"SELECT 'Hello World';")
#
