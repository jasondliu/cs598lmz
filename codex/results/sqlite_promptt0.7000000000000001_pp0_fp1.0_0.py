import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def test_connect_basic():
    """
    Tests the basic connect functionality
    """
    def _test_connect(kwargs):
        conn = sqlite3.connect(**kwargs)
        assert conn.execute("select 1").fetchone()[0] == 1
        conn.close()
    _test_connect({})
    _test_connect({'database': ''})
    _test_connect({'database': ':memory:'})

def test_connect_with_uri():
    """
    Tests the connect functionality with URI's
    """
    def _test_connect(uri):
        conn = sqlite3.connect(uri)
        assert conn.execute("select 1").fetchone()[0] == 1
        conn.close()
    _test_connect('file::memory:?cache=shared')
    _test_connect('file:?mode=memory&cache=shared')
    _test_connect('file::memory:?mode=memory&cache=shared')
    _test_connect('file::memory:?cache=shared&mode=memory')
