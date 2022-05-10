import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('create table test(i, j)').
# fetchall()
from . import sqlite3_util
from . import sqlite3_map

# Needed to properly do json encoding / decoding
from . import json

def test_sqlite3():
    encodefunc = bytefunc_to_strfunc(sqlite3.encodestring)
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('create table test(i, j)')
    c.executemany('insert into test values (?, ?)',
                  [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])
    # Start a transaction that gets rolled back
    conn.execute('create table test2(i, j)')
    conn.execute('insert into test2 values(2, 3)')
    conn.execute('create table test3(i, j)')
    conn.execute('insert into test3 values(3, 4)')
