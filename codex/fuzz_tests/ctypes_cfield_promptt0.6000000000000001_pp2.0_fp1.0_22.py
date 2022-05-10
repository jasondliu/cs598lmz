import ctypes
# Test ctypes.CField
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["foo"]
    _fields_ = [("foo", ctypes.c_int * 3)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["foo"]
    _fields_ = [("foo", ctypes.c_int * 3)]
    _anonymous_ = ["bar"]
    _fields_ = [("bar", ctypes.c_int * 3)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["foo"]
    _fields_ = [("foo", ctypes.c_int * 3)]
    _anonymous_ = ["bar"]
    _
