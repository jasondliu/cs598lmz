import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute('create table test(id integer primary key, name text)')
# c.execute('insert into test(name) values (?)', ('foo',))
# c.execute('insert into test(name) values (?)', ('bar',))
# c.execute('select * from test')
# print(c.fetchall())
# conn.commit()
# conn.close()

# Test ctypes
# libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
# print(libc.time(None))

# Test threading
# def worker():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(2)
#     print(threading.currentThread().getName(), 'Exiting')

# def my_service():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(3)
#     print(threading.
