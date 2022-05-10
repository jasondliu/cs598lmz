import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''create table stocks
             (date text, trans text, symbol text, qty real, price real)''')
c.execute("""insert into stocks
                  values ('2006-01-05','BUY','RHAT',100,35.14)""")
conn.commit()
c.close()

# Test ctypes.util.find_library
libc = ctypes.util.find_library('c')
print(libc)

# Test threading.Thread
def f():
    print('hello world')

t = threading.Thread(target=f)
t.start()
t.join()

# Test ctypes.CDLL
libc = ctypes.CDLL(libc)
libc.printf(b'Hello, World!\n')
