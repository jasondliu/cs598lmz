import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# conn.commit()
# conn.close()
#
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print c.fetchone()
# conn.close()

# Test ctypes
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# message_string = 'Hello World!\n'
# libc.printf('Testing: %s', message_string)

# Test threading
# def worker():
#     print threading.currentThread().getName(), 'Starting'
#    
