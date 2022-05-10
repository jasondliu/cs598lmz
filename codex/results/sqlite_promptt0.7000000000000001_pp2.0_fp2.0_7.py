import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() and sqlite3.Connection.close()

def callback(s, t, d, p):
    pass

def thd(i):
    for j in range(1000):
        sqlite3.connect(":memory:").close()

threads = []
for i in range(4):
    t = threading.Thread(target=thd, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("done")

# Test sqlite3.connect() and sqlite3.Connection.close() with thread-safe enabled

def callback(s, t, d, p):
    pass

def thd(i):
    for j in range(1000):
        sqlite3.connect(":memory:", check_same_thread=False).close()

threads = []
for i in range(4):
    t = threading.Thread(target=thd, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
   
