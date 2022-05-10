import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(), sqlite3.Cursor.execute(), sqlite3.Cursor.fetchall(), sqlite3.Cursor.close()
def sqlite3_test():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

# Test threading.Lock
def threading_test():
    lock = threading.Lock()
    lock.acquire()
    lock.release()

# Test ctypes.util.find_library
def ctypes_test():
    print(ctypes.util.find_library('c'))

# Test ctypes.CDLL
