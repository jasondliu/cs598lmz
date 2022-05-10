import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.iterdump()

def check_dump(dump, expected):
    dump = dump.strip().splitlines()
    expected = expected.strip().splitlines()
    assert len(dump) == len(expected)
    for d, e in zip(dump, expected):
        assert d == e, "%r != %r" % (d, e)

def CheckIsolation(dbname):
    def Write():
        c = get_thread_conn().cursor()
        c.execute('create table tbl(x)')
        c.execute('insert into tbl(x) values (1)')
        c.execute('begin')
        c.execute('insert into tbl(x) values (2)')
        c.execute('insert into tbl(x) values (2)')
        c.execute('commit')
        c.execute('select * from tbl')
        print(c.fetchall())

    def Read():
        c = get_thread_conn().cursor()
        with c:
            c.execute('select * from tbl')
            assert [(1
