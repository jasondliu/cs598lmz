import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('create table test(id int)')
cur.execute('insert into test(id) values (1)')
cur.execute('select id from test')
print(cur.fetchone()[0])
cur.close()
con.close()
# Test ctypes.util.find_library
print(ctypes.util.find_library('m'))
# Test ctypes.CDLL
libc = ctypes.CDLL(ctypes.util.find_library('c'))
print(libc.abs(-1))
# Test threading.Thread
class MyThread(threading.Thread):
    def run(self):
        print('hello from a thread')
t = MyThread()
t.start()
t.join()
