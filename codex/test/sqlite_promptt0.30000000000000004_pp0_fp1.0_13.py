import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect('example.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#conn.commit()
#conn.close()

#print(ctypes.util.find_library('c'))

#libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
#print(libc.getpid())

#print(ctypes.util.find_library('m'))

#libm = ctypes.CDLL(ctypes.util.find_library('m'), use_errno=True)
#print(libm.cos(0.5))

#print(ctypes.util.find_library('pthread'))

#libpthread = ctypes.CDLL(ctypes.util.find
