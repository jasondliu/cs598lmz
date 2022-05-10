import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')
#conn = sqlite3.connect('/home/pi/Desktop/test.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# Test sqlite3.connect
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM stocks")
print cursor.fetchall()
conn.close()
