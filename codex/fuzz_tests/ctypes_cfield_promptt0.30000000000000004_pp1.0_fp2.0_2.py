import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

class XX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("x", X)]

class YY(ctypes.Structure):
    _fields_ = [("x", XX),
                ("y", ctypes.c_int)]

class ZZ(ctypes.Structure):
    _fields_ = [("y", YY),
                ("z", ctypes.c_int)]

class XXX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_
