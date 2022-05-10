import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:").execute("drop table if exists fts4_test").fetchall()
import multiprocessing

test_lock = threading.Lock()


def sync_commit(func):
    def wrapper(*args):
        test_lock.acquire()
        try:
            func(*args)
        finally:
            test_lock.release()
    return wrapper


