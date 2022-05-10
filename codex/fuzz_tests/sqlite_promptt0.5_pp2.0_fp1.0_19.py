import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect(':memory:')
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#conn.commit()
#c.execute('SELECT * FROM stocks')
#print(c.fetchall())
#conn.close()

# Test ctypes.util
#print(ctypes.util.find_library('c'))

# Test ctypes
libc = ctypes.CDLL(ctypes.util.find_library('c'))
print(libc.time(None))


def thread_function(name):
    print("Thread %s: starting" % name)
    time.sleep(2)
    print("Thread %s: finishing" % name)


if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args
