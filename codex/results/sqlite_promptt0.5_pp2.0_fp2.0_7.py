import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

db = sqlite3.connect(':memory:')
cursor = db.cursor()
cursor.execute('CREATE TABLE person (firstname, lastname)')
cursor.execute('INSERT INTO person VALUES ("John", "Smith")')
cursor.execute('SELECT * FROM person')
print(cursor.fetchall())

cursor.close()
db.close()

# Test ctypes.util.find_library
print(ctypes.util.find_library('c'))
# Test ctypes.CDLL

libc = ctypes.CDLL(ctypes.util.find_library('c'))
print(libc.strlen('Hello, world!'))
# Test threading.Lock

lock = threading.Lock()

lock.acquire()
print('Lock acquired.')
lock.release()
print('Lock released.')
 
# Test threading.Thread

class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.
