import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() and sqlite3.Connection.cursor() and sqlite3.Cursor.execute()
# Test sqlite3.Connection.close()

# db = sqlite3.connect(":memory:")
db = sqlite3.connect('/tmp/test.db')
c = db.cursor()
c.execute('''CREATE TABLE stocks
(date text, trans text, symbol text, qty real, price real)''')

# Test sqlite3.Cursor.commit()
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
db.commit()

# Test sqlite3.Cursor.fetchone(), sqlite3.Cursor.fetchmany(), and sqlite3.Cursor.fetchall()
