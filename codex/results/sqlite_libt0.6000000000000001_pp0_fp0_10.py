import ctypes
import ctypes.util
import threading
import sqlite3
import os

def get_libc():
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.malloc.restype = ctypes.c_void_p
    libc.malloc.argtypes = [ctypes.c_size_t]
    libc.free.restype = None
    libc.free.argtypes = [ctypes.c_void_p]
    libc.memmove.restype = ctypes.c_void_p
    libc.memmove.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
    return libc

libc = get_libc()

def memmove(dest, src, length):
    libc.memmove(dest, src, length)

def malloc(size):
    return libc.malloc(size)

def free(p):
    libc.free(p)

def get_sqlite_lib():
    libsqlite =
