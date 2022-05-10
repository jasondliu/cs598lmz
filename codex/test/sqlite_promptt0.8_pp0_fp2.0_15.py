import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
# Create in-memory database.
sqlite3.connect(':memory:')
# Create file database.
sqlite3.connect('/path/to/database.db')
# Open database.
# Create table.
conn.execute('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')
# Insert a row of data.
conn.execute('INSERT INTO stocks VALUES ("2006-01-05","BUY","RHAT",100,35.14)')
# Save (commit) the changes.
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
# Insert a row of data.
conn.execute('INSERT INTO stocks VALUES ("2006-01-05","BUY","RHAT",100,35.14)')
# Do this instead.
t = ('RHAT',)
sql = 'SELECT * FROM stocks WHERE symbol = ?'
