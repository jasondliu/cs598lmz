import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() in multi-thread
conn = sqlite3.connect('test_thread.db')
print 'db connection is ready'

start = time.time()
t_list = []
for i in range(10):
    t = threading.Thread(target=loop, args=(conn, i, ))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()
print time.time() - start
