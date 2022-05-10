import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/test.db')

class _C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class _D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class _E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)]

class _F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int),
                ('e', ctypes.c_int)]

class _G(ctypes.Structure
