import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
print (conn)
c = conn.cursor()
c.execute(''' CREATE TABLE  IF NOT EXISTS stocks (date text, trans text, symbol text,qty real,price real) ''')
# C has the data connection
# r is the test values
t=('2006-03-28','BUY','RHAT',100,35.14)
c.execute('INSERT INTO stocks VALUES (?,?,?,?,?)',t)
conn.commit()
c.execute('''SELECT * FROM stocks''')
row= c.fetchall()
print (row)

# c.execute(''' INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14) ''')
# c.execute(''' INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14) ''')
# c.execute(''' INSERT INTO stocks VALUES ('2006-03-28','BUY','RHAT',100,35.
