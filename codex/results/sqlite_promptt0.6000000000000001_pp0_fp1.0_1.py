import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.Cursor.execute

# load the sqlite3 library
sqlite3.load_extension('/usr/local/lib/libsqlitefunctions.dylib')

# connect to database
conn = sqlite3.connect('../data/test.db')

# create a cursor
c = conn.cursor()

# create a table
try:
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')
except sqlite3.OperationalError:
    print 'Table already exists'

# insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# save the changes
conn.commit()

# close the connection
conn.close()

# create a connection
conn = sqlite3.connect('../data/test.db')

# create a cursor
c = conn.cursor()

# execute a query
c.execute("SELECT * FROM stocks")

#
