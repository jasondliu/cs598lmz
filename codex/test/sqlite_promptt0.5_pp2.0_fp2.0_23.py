import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')

# https://github.com/python/cpython/blob/master/Modules/posixmodule.c
_libc = ctypes.CDLL(ctypes.util.find_library('c'))
_libc.pthread_atfork.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

def _on_fork():
    # Close all open database connections, because fork() doesn't
    # copy open file descriptors.
    sqlite3.connect(':memory:').close()

_libc.pthread_atfork(None, None, _on_fork)

def main():
    db = sqlite3.connect('file::memory:?cache=shared')
    db.execute('create table t (c)')
    db.execute('insert into t values (?)', ('x',))
    db.execute('insert into t values (?)', ('y',))
    db.commit()
