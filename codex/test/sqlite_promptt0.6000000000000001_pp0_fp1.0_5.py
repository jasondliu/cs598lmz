import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Open and read a file.
f = open('/home/yh/workspace/python/sqlite/test_sqlite3.py','r')
#f.read()

# Open a connection to a database file.
conn = sqlite3.connect('/home/yh/workspace/python/sqlite/test.db')
c = conn.cursor()

# Create a table.
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data.
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes.
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
# Test sqlite3.execute()
