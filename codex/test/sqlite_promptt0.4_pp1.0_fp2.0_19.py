import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

def test_connect():
    # Connect to a database.
    con = sqlite3.connect(":memory:")
    con.close()

def test_connect_bad_args():
    # Connect to a database with a non-string name.
    try:
        con = sqlite3.connect(None)
    except TypeError:
        pass
    else:
        con.close()
        raise Exception("connect() with non-string name should fail")

def test_connect_bad_args2():
    # Connect to a database with a non-string name.
    try:
        con = sqlite3.connect(None)
    except TypeError:
        pass
    else:
        con.close()
        raise Exception("connect() with non-string name should fail")

def test_connect_bad_args3():
    # Connect to a database with a non-string name.
    try:
        con = sqlite3.connect(None)
    except TypeError:
        pass
    else:
        con.close()
