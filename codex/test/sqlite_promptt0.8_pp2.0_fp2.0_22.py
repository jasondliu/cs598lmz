import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.enable_load_extension(True) for load_extension
# before running this script.
import os

DIR = os.path.dirname(os.path.abspath(__file__))
libname = '../lib/libsqlite3ifp.so'
lib = '%s/%s' % (DIR, libname)
so = ctypes.cdll.LoadLibrary(lib)

def store_blob(conn, filename):
    conn.execute('CREATE TABLE IF NOT EXISTS tbl_blob(name TEXT, content BLOB)')
    name = os.path.basename(filename)
    with open(filename, 'rb') as f:
        content = f.read()
        conn.execute('''
            INSERT INTO tbl_blob(name, content) VALUES(?, ?)''', (name, content))
    print('Loaded %s' % filename)

def load_blob(conn, filename):
    cur = conn.execute('SELECT content FROM tbl_blob WHERE name=?', (filename,))

