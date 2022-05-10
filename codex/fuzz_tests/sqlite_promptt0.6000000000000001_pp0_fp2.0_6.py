import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memorydb?mode=memory&cache=shared', uri=True)
import sys
import time

# SQLITE_THREADSAFE
# SQLITE_OPEN_NOMUTEX
# SQLITE_OPEN_FULLMUTEX
# SQLITE_OPEN_SHAREDCACHE
# SQLITE_OPEN_PRIVATECACHE

lock = threading.Lock()

sqlite3._sqlite3.sqlite3_enable_shared_cache(1)

# sqlite3.enable_shared_cache(True)

def run(fn):
    with lock:
        with sqlite3.connect('file:memorydb?mode=memory&cache=shared', uri=True) as db:
            fn(db)

def run_many(fn, count):
    threads = []
    for i in range(count):
        t = threading.Thread(target=run, args=(fn,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def
