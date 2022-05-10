import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def test_sqlite3_connect():
    conn = sqlite3.connect(':memory:')
    assert conn
    conn.close()

# Test sqlite3.connect() with a file

def test_sqlite3_connect_file():
    import os
    try:
        os.unlink('test.db')
    except:
        pass
    conn = sqlite3.connect('test.db')
    assert conn
    conn.close()
    os.unlink('test.db')

# Test sqlite3.connect() with a file and timeout

def test_sqlite3_connect_file_timeout():
    import os
    try:
        os.unlink('test.db')
    except:
        pass
    conn = sqlite3.connect('test.db', timeout=1)
    assert conn
    conn.close()
    os.unlink('test.db')

# Test sqlite3.connect() with a file and isolation_level

