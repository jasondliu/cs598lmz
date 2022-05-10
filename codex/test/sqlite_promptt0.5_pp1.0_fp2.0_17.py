import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")
# Test sqlite3.Cursor
c = conn.cursor()
# Test sqlite3.Cursor.execute
c.execute("CREATE TABLE foo (bar int)")
# Test sqlite3.Cursor.executemany
c.executemany("INSERT INTO foo VALUES (?)", [(1,), (2,), (3,)])
# Test sqlite3.Cursor.executescript
c.executescript("""
    CREATE TABLE bar (baz int);
    INSERT INTO bar VALUES (4);
""")
# Test sqlite3.Cursor.fetchone
c.execute("SELECT * FROM foo")
c.fetchone()
# Test sqlite3.Cursor.fetchmany
c.fetchmany(2)
# Test sqlite3.Cursor.fetchall
c.fetchall()
# Test sqlite3.Cursor.close
c.close()
# Test sqlite3.Cursor.__iter__
