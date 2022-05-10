import ctypes
# Test ctypes.CField

import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char),
                ("d", ctypes.c_char),
                ("e", ctypes.c_double)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char),
                ("d", ctypes.c_char),
                ("e", ctypes.c_double),
                ("f", ctypes.c_int),
                ("g", ctypes.c_char)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char),
                ("d", ctypes.c_char),
                ("e", ctypes.
