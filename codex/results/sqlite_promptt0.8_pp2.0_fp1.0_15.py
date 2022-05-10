import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, .cursor and .commit
db = sqlite3.connect('test.db')
cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS main.TestData(id INTEGER PRIMARY KEY, value INTEGER);')
cur.execute('INSERT INTO main.TestData(value) VALUES(?);', (2000000000,))
cur.execute('INSERT INTO main.TestData(value) VALUES(?);', (3000000000,))
cur.execute('INSERT INTO main.TestData(value) VALUES(?);', (6000000000,))
db.commit()

cur.execute('SELECT * FROM main.TestData ORDER BY id ASC;')
print cur.fetchall()

# Test lib.sqlite3_initialize
libname = ctypes.util.find_library('sqlite3')
if libname:
    lib = ctypes.CDLL(libname)
else:
    lib = None

if lib:
    lib.sqlite3_initialize()
    # Test sqlite3.connect, .
