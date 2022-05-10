import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
# Get a cursor object
cursor = conn.cursor()
cursor.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, 
             qty real, price real)''')
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
t = ('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
print cursor.fetchone()
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
cursor.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
        print row
