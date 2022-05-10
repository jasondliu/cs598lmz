import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() and sqlite3.Connection()
print(sqlite3.connect)
print(sqlite3.Connection)

# Test sqlite3.connect()
print(sqlite3.connect(':memory:'))

# Test sqlite3.connect() with database file
con = sqlite3.connect('test.db')
print(con)

# Test sqlite3.connect() with database file
con = sqlite3.connect('test.db')
# Test sqlite3.Connection.cursor()
cur = con.cursor()
print(cur)

# Test sqlite3.connect() with database file
con = sqlite3.connect('test.db')
# Test sqlite3.Connection.execute()
con.execute('select 1')

# Test sqlite3.connect() with database file
con = sqlite3.connect('test.db')
# Test sqlite3.Connection.executescript()
con.executescript('select 1; select 2')

# Test sqlite3.connect() with database file
con = sqlite3.connect('test.db')

