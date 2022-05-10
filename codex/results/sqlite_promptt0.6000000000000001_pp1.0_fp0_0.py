import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE test (id integer primary key, count integer)")
c.execute("INSERT INTO test (count) VALUES (1)")
c.execute("INSERT INTO test (count) VALUES (2)")
c.execute("INSERT INTO test (count) VALUES (3)")
c.execute("SELECT count FROM test")
print(c.fetchall())
c.execute("SELECT count FROM test WHERE id = 1")
print(c.fetchone())
conn.commit()
conn.close()

# Test ctypes.util.find_library()
print(ctypes.util.find_library('c'))
print(ctypes.util.find_library('m'))
print(ctypes.util.find_library('pthread'))

# Test threading.Lock()
lock = threading.Lock()
lock.acquire()
lock.release()
