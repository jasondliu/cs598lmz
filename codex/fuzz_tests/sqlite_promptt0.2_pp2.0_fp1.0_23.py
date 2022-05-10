import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# Test sqlite3.connect

def test_connect():
    conn = sqlite3.connect(':memory:')
    conn.close()

def test_connect_kwargs():
    conn = sqlite3.connect(database=':memory:')
    conn.close()

def test_connect_uri():
    conn = sqlite3.connect('file:test?mode=memory&cache=shared')
    conn.close()

def test_connect_uri_kwargs():
    conn = sqlite3.connect('file:test?mode=memory&cache=shared', uri=True)
    conn.close()

def test_connect_uri_kwargs_false():
    conn = sqlite3.connect('file:test?mode=memory&cache=shared', uri=False)
    conn.close()

def test_connect_uri_kwargs_invalid():
    try:
        conn = sqlite3.connect('file:test?mode=memory&cache=shared', uri='invalid')
    except TypeError:
        pass
   
