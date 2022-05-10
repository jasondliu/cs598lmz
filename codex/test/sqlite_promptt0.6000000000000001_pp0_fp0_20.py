import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class C(ctypes.Structure):
    _fields_ = [('id', ctypes.c_int),
                ('name', ctypes.c_char_p),
                ('value', ctypes.c_double),
                ('blob', ctypes.c_void_p),
                ('blob_size', ctypes.c_int),
                ('c2', ctypes.c_void_p),
                ('c3', ctypes.c_void_p),
               ]

C_pointer = ctypes.POINTER(C)

class C2(ctypes.Structure):
    _fields_ = [('id', ctypes.c_int),
                ('name', ctypes.c_char_p),
                ('value', ctypes.c_double),
                ('blob', ctypes.c_void_p),
                ('blob_size', ctypes.c_int),
                ('c', ctypes.c_void_p),
                ('c3', ctypes.c_void_p),
               ]


