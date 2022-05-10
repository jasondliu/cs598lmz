import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()
conn.close()

import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM stocks ORDER BY price'
