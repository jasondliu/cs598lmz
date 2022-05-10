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

# Test ctypes.util.find_library
# print(ctypes.util.find_library('c'))

# Test ctypes.CDLL
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# print(libc)
# print(libc.time)
# print(libc.time(None))

# Test ctypes.CDLL.__getattr__
# print(libc.time)
# print(libc.time(None))

# Test ctypes.CDLL.__getattr__
# print(libc.printf)
# print(libc.printf("Hello
