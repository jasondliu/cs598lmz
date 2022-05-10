import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("d", ctypes.c_int)]

class XX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class YY(ctypes.Structure):
    _fields_ = [("x", XX),
                ("c", ctypes.c_int)]

class ZZ(ctypes.Structure):
    _fields_ = [("y", YY),
                ("d", ctypes.c_int)]

class XXX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b",
