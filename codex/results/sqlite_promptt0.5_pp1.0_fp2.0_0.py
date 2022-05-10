import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

def test_connect():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("create table test(i)")
    cur.execute("insert into test(i) values (1)")
    cur.execute("select i from test")
    assert cur.fetchone()[0] == 1
    cur.close()
    con.close()

def test_connect_factory():
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    con = sqlite3.connect(":memory:", factory=dict_factory)
    cur = con.cursor()
    cur.execute("create table test(i)")
    cur.execute("insert into test(i) values (1)")
    cur.execute("select i from test")
    assert cur.fetchone()["i"] == 1
