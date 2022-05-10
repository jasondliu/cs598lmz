import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()
# Test sqlite3.connect
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("SELECT * FROM stocks")
print(c.fetchall())
conn.close()

# Test os.system
import os
os.system("ls")

# Test os.getenv
import os
print(os.getenv('PATH'))

# Test os.getcwd
import os
print(os.getcwd())

# Test os.chdir
import os
os.chdir("/tmp")
print(os.getcwd())

# Test os.listdir

