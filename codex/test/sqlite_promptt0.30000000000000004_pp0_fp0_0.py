import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

def test_connect():
    try:
        conn = sqlite3.connect(':memory:')
        conn.close()
    except:
        assert False, 'connect() failed'

def test_connect_kwargs():
    try:
        conn = sqlite3.connect(database=':memory:')
        conn.close()
    except:
        assert False, 'connect() failed'

def test_connect_uri():
    try:
        conn = sqlite3.connect('file::memory:?cache=shared')
        conn.close()
    except:
        assert False, 'connect() failed'

def test_connect_uri_kwargs():
    try:
        conn = sqlite3.connect('file::memory:?cache=shared', uri=True)
        conn.close()
    except:
        assert False, 'connect() failed'

