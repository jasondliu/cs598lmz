import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Create a connection object to the database
conn = sqlite3.connect('test.db')

# Create a cursor object
c = conn.cursor()

# Execute the CREATE TABLE statement
c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# Test sqlite3.connect()

# Create a connection object to the database
conn = sqlite3.connect('test.db')

# Create a cursor object
c = conn.cursor()

# Execute the SELECT statement
c.execute("SELECT * FROM stocks")

# Fetch the results
results = c.fetchall()

# Print
