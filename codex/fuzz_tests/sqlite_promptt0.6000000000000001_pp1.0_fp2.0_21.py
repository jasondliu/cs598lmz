import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

#sqlite3.threadsafety = 1
sqlite3.threadsafety = 2

# XXX: We should really be using SQLite's threading mode 2
# but that makes the database go corrupt all the time.
# For now, just make sure we can switch modes without
# crashing.

def test_threadsafety():
    # Test that switching thread safety modes works
    conn = sqlite3.connect(':memory:')
    assert conn.isolation_level == None
    assert conn.threadsafety == sqlite3.threadsafety
    cursor = conn.cursor()
    cursor.execute("create table test(i)")
    cursor.execute("insert into test(i) values (1)")
    cursor.execute("insert into test(i) values (2)")
    cursor.execute("select i from test")
    assert cursor.fetchall() == [(1,), (2,)]
    conn.close()

def test_connect():
    # Test basic connection
    conn = sqlite3.connect(':memory:')
    assert conn.isolation_
