import ctypes
import ctypes.util
import threading
import sqlite3
import hashlib

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
libc.strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
libc.strcmp.restype = ctypes.c_int

def lookup_user_pass(container_path, username):
    dbhash = hashlib.sha256()
    dbhash.update(username)
    dbhash.update(butils.random_string(4))
    dbhash = dbhash.hexdigest()

    dbpath = os.path.join(container_path, 'users', dbhash)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute('create table if not exists users (username text, password text)')
    cursor.execute('insert or ignore into users values (?, ?)', (username, butils.random_string(32)))
    cursor.execute('select password from users where username = ?', (username,))
    r = cursor
