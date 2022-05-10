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

# Test ctypes
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# print(libc.time(None))

# Test threading
# def worker():
#     print(threading.current_thread().getName(), 'Starting')
#     time.sleep(2)
#     print(threading.current_thread().getName(), 'Exiting')

# def my_service():
#     print(threading.current_thread().getName(), 'Starting')
#     time.sleep(3)
#     print(threading.current_thread().getName(), 'Exiting')

#
