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


def test_redundant_idx_create():
    # Test that the redundant idx is created when the schema supports it.
    # Within each group, the first item (idx=0) is a FTS4 table, the second
    # (idx=1) is a FTS4 table with the "redundant_idx" set to False, and the
    # third (idx=2) is a FTS5 table.
    #
    # The 'redundant_idx' option is only applicable to FTS4 tables. A FTS5 table
    # may or may not have a redundant index, depending on the value of the
    # 'detail=columns' option to the f
