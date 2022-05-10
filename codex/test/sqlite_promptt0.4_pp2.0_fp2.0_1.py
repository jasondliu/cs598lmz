import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# Test sqlite3.connect

def test_connect():
    db = sqlite3.connect(":memory:")
    db.close()

def test_connect_kwargs():
    db = sqlite3.connect(database=":memory:")
    db.close()

def test_connect_uri():
    db = sqlite3.connect("file:test?mode=memory&cache=shared")
    db.close()

def test_connect_uri_kwargs():
    db = sqlite3.connect(database="file:test?mode=memory&cache=shared")
    db.close()

def test_connect_uri_filename():
    db = sqlite3.connect("file:test?mode=memory&cache=shared", uri=True)
    db.close()

def test_connect_uri_filename_kwargs():
    db = sqlite3.connect(database="file:test?mode=memory&cache=shared", uri=True)
    db.close()

