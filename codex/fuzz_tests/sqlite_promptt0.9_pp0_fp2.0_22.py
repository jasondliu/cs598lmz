import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() statement in Python console
# This stores the results of the stock analysis in a sqlite3 database
database = r'C:\Users\Lucifer.Gregory\Desktop\Code\HackerRank\Developer Mountain\Concurrency\test\test_db.db'
conn = sqlite3.connect(database)
conn.text_factory = str

# Test conn.cursor().execute() statement in Python console
curs = conn.cursor()
# tables = curs.execute('''SELECT NAME FROM SQLITE_MASTER''')

# Test table check
# for table in tables:
#   if table[0] == 'stocks':
#       print 'Yay'

# cursor.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')

# cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Test curs.executemany() statement in Python console
t = ('RHAT',)
# cursor.execute('SELECT * FROM
