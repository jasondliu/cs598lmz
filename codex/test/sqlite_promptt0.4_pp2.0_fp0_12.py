import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect('/home/pi/Desktop/test.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#conn.commit()
#conn.close()

# Test lib
try:
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
except OSError:
    print('cannot find libc')

try:
    libm = ctypes.CDLL(ctypes.util.find_library('m'))
except OSError:
    print('cannot find libm')

try:
    libpthread = ctypes.CDLL(ctypes.util.find_library('pthread'))
except OSError:
    print('cannot find libpthread')

