import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

def test_connect():
    # Test sqlite3.connect()
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("create table test(i)")
    cur.execute("insert into test(i) values (1)")
    cur.execute("select i from test")
    assert cur.fetchone()[0] == 1
    cur.execute("select i from test")
    assert cur.fetchone()[0] == 1
    cur.execute("select i from test")
    assert cur.fetchone()[0] == 1
    con.close()

def test_connect_kwargs():
    con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    cur.execute("create table test(ts timestamp)")
    cur.execute("insert into test(ts) values (?)", (datetime.datetime.now(),))
    cur
