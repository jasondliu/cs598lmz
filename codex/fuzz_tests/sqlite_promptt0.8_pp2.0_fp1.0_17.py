import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
#conn = sqlite3.connect(':memory:')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')
#conn = sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
conn = sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True, check_same_thread=False)
cur1 = conn.cursor()
cur2 = conn.cursor()

def writer():
    for i in range(1, 100):
        cur1.execute('INSERT INTO test VALUES (?)', (i,))
        conn.commit()

def reader():
    for i in range(1, 100):
        cur2.execute('SELECT * FROM test')
        print(cur2.fetchone())


t1 = threading.Thread(target=writer)
t1.daemon = True
t1.start()
t2 = threading.Thread(target=reader)
t2.daemon = True
