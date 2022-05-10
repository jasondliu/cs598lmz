import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect(':memory:')
#c = conn.cursor()
#c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
#c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
#conn.commit()
#c.close()
#conn.close()

# Test ctypes.util.find_library
#print ctypes.util.find_library('c')

# Test threading.Lock
lock = threading.Lock()
lock.acquire()
lock.release()

# Test re.MULTILINE
