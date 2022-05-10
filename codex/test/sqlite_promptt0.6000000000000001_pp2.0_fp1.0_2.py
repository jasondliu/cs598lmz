import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
def test_connect():
    db = sqlite3.connect(":memory:")
    print(db)
    db.close()

# Test sqlite3.Row
def test_row():
    db = sqlite3.connect(":memory:")
    db.execute("create table person(firstname, lastname)")
    db.execute("insert into person(firstname, lastname) values (?, ?)", ("foo", "bar"))
    db.execute("insert into person(firstname, lastname) values (?, ?)", ("baz", "qux"))
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from person")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row["lastname"])
    db.close()

# Test sqlite3.Cursor.executemany()
def test_executemany():
    db = sqlite3.connect(":memory:")
