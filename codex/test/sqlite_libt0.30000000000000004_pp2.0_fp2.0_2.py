import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

# This is a hack to make sure that the database is only opened once.
# We need to do this because the database is not thread safe and
# we want to make sure that we don't get any errors when we try to
# access it from multiple threads.
_db_lock = threading.Lock()
_db_connection = None
_db_cursor = None

# This is a hack to make sure that the database is only opened once.
# We need to do this because the database is not thread safe and
# we want to make sure that we don't get any errors when we try to
# access it from multiple threads.
_db_lock = threading.Lock()
_db_connection = None
_db_cursor = None

def _get_db_cursor():
    global _db_connection, _db_cursor
    if _db_cursor is None:
        _db_lock.acquire()
