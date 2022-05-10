import ctypes
# Test ctypes.CField

import sys

if sys.platform == 'win32':
    libc = ctypes.CDLL('msvcrt')
else:
    libc = ctypes.CDLL(None)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int)]

class POINTER(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(X))]

class POINTER2(ctypes.Structure):
    _fields_ =
