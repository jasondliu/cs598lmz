import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def test_sqlite3_connect():
    conn = sqlite3.connect(":memory:")
    conn.close()

# Test sqlite3.connect(":memory:")

def test_sqlite3_connect_memory():
    conn = sqlite3.connect(":memory:")
    conn.close()

# Test sqlite3.connect("file:memory:?cache=shared")

def test_sqlite3_connect_memory_shared():
    conn = sqlite3.connect("file:memory:?cache=shared")
    conn.close()

# Test sqlite3.connect("file:memory:?cache=private")

def test_sqlite3_connect_memory_private():
    conn = sqlite3.connect("file:memory:?cache=private")
    conn.close()

# Test sqlite3.connect("file:memory:?cache=private", uri=True)

def test_sqlite3_connect_memory_private_uri():
    conn = sqlite3.connect("file:memory:?cache=
