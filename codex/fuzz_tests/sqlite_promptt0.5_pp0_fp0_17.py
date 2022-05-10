import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def test_sqlite3_connect():
    """
    >>> sqlite3.connect(':memory:').close()
    """

# Test sqlite3.Connection.close()

def test_sqlite3_Connection_close():
    """
    >>> c = sqlite3.connect(':memory:')
    >>> c.close()
    """

# Test sqlite3.Connection.cursor()

def test_sqlite3_Connection_cursor():
    """
    >>> c = sqlite3.connect(':memory:')
    >>> c.cursor().close()
    >>> c.close()
    """

# Test sqlite3.Connection.commit()

def test_sqlite3_Connection_commit():
    """
    >>> c = sqlite3.connect(':memory:')
    >>> c.commit()
    >>> c.close()
    """

# Test sqlite3.Connection.rollback()

def test_sqlite3_Connection_rollback():
    """
    >>> c = sqlite3.connect(':memory:
