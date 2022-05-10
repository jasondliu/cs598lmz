import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('example.db')
# c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# conn.commit()
# conn.close()

# Test ctypes.util.find_library
# print(ctypes.util.find_library('c'))
# print(ctypes.util.find_library('m'))

# Test os.path.exists
print(os.path.exists('example.db'))

# Test os.remove
# os.remove('example.db')

# Test threading
# def worker():
#     """thread worker function"""
#     print('Worker')
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()
