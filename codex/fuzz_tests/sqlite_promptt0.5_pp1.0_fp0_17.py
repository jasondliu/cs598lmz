import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#import sqlite3
#conn = sqlite3.connect('example.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#conn.commit()
#conn.close()

#c = conn.cursor()
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print(c.fetchone())

# Locate the libc shared library.
libc_path = ctypes.util.find_library('c')
if not libc_path:
    raise Exception('Failed to find libc')

# Load the shared library into ctypes.
libc = ctypes.CDLL(libc_path)

# The prototype of the function we're going to call.
# The arguments and return types are defined here,
# and the actual name
