import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def test_connect():
    conn = sqlite3.connect(":memory:")
    conn.close()

def test_connect_kwargs():
    conn = sqlite3.connect(database=":memory:")
    conn.close()

def test_connect_uri():
    conn = sqlite3.connect("file::memory:?cache=shared")
    conn.close()

def test_connect_uri_kwargs():
    conn = sqlite3.connect("file::memory:?cache=shared", uri=True)
    conn.close()

def test_connect_uri_kwargs_fail():
    raises(sqlite3.ProgrammingError, sqlite3.connect,
        "file::memory:?cache=shared", uri=False)

def test_connect_uri_kwargs_fail_2():
    raises(sqlite3.ProgrammingError, sqlite3.connect,
        "file::memory:?cache=shared", uri=True, database=":memory:")

def test_connect_uri_kwargs_fail
