import ctypes
import ctypes.util
import threading
import sqlite3
import _sqlite3
import os
import sys


_LOCK = threading.Lock()


_sqlite_synchronous = {
    0: 'OFF',
    1: 'NORMAL',
    2: 'FULL',
}


_sqlite_temp_store = {
    0: 'DEFAULT',
    1: 'FILE',
    2: 'MEMORY',
}


def _synchronous(conn):
    # Work around CPython bug #15973
    synchronous = conn.execute("PRAGMA synchronous;").fetchone()[0]
    return _sqlite_synchronous[synchronous]


def _temp_store(conn):
    # Work around CPython bug #15973
    temp_store = conn.execute("PRAGMA temp_store;").fetchone()[0]
    return _sqlite_temp_store[temp_store]


_KEY = {
    'synchronous': _synchronous,
    'temp_store': _temp_store,
}


