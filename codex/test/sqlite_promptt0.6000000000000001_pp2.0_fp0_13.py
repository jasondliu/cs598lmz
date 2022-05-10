import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect function

# If a database file exists, create a connection to it
conn = sqlite3.connect('test.db')
# Create a cursor
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
# Test sqlite3.execute function

# If a database file exists, create a connection to it
conn = sqlite3.connect('test.db')
# Create a cursor
c = conn.cursor()

# Create a table if it doesn't exist
