import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

def get_libc():
    libc_path = ctypes.util.find_library('c')
    if not libc_path:
        raise RuntimeError('Cannot find libc')
    return ctypes.CDLL(libc_path)

def get_libpthread():
    libpthread_path = ctypes.util.find_library('pthread')
    if not libpthread_path:
        raise RuntimeError('Cannot find libpthread')
    return ctypes.CDLL(libpthread_path)

def get_libsqlite3():
    libsqlite3_path = ctypes.util.find_library('sqlite3')
    if not libsqlite3_path:
        raise RuntimeError('Cannot find libsqlite3')
    return ctypes.CDLL(libsqlite3_path)

def get_libsqlite3_so():
    libsqlite3_path = ctypes.util.find_library('sqlite3')
    if not libsqlite3_path:
        raise Runtime
