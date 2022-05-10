import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# sqlite3.connect('test.db')

# Test ctypes.util.find_library()
# print ctypes.util.find_library('c')

print threading.current_thread()

# Test ctypes.CDLL()
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# print libc

# Test ctypes.CDLL().getnid()
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# print libc.getpid()

# Test sqlite3.connect().cursor()
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()

# Test sqlite3.connect().cursor().execute()
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.close()

# Test sqlite3.connect().cursor().
