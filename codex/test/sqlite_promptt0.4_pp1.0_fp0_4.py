import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect(":memory:")
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#conn.commit()
#c.execute("SELECT * FROM stocks")
#print c.fetchall()
#conn.close()

# Test ctypes
libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.printf("Hello, %s\n", "World!")

# Test threading
