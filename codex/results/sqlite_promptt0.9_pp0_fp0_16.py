import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect


@threads(2)
def test_connect1(n):
    try:
        db = sqlite3.connect(':memory:')
        c = db.cursor()
        c.execute("CREATE TABLE foo(id INTEGER PRIMARY KEY,bar)")
        for i in xrange(1000):
            c.execute("INSERT INTO foo VALUES (NULL,?)", (i,))
        c.execute("SELECT COUNT(*) FROM foo")
        assert c.fetchone() == (1000,)
    finally:
        db.close()

# Test Other than sqlite3.connect


@threads(2)
def test_connect2(n):
    try:
        db = sqlite3.connect(':memory:')
        c = db.cursor()
        c.execute("CREATE TABLE foo(id INTEGER PRIMARY KEY,bar)")
        for i in xrange(1000):
            c.execute("INSERT INTO foo VALUES (NULL,?)", (i,))
        c.execute("SELECT COUNT(*)
