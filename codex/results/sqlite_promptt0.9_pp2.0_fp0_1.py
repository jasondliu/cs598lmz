import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections

_sqlite = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
# _sqlite.sqlite3_threadsafe.restype = ctypes.c_int
# if _sqlite.sqlite3_threadsafe():
#     print('Threadsafe')
# else:
#     raise Exception('Not threadsafe')
# We hope it is threadsafe

def sqlite_op(db_file):
    print('Init Connection', threading.get_ident())
    conn = sqlite3.connect(db_file, check_same_thread=True)
    print('Shared Connection', id(conn), threading.get_ident())
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    print('Select 1', id(conn), threading.get_ident())
    print(cursor.fetchall())
    conn.close()
    print('Close Connection', threading.get_ident())

db_file = r'C:\sqlite3_test.db'


conn = sqlite3
