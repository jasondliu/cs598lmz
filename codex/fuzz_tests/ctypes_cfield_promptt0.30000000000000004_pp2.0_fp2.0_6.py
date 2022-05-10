import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

class Z(X, Y):
    _fields_ = [("c", ctypes.c_int)]

class XX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class YY(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class ZZ(XX, YY):
    _fields_ = [("e", ctypes.c_int),
                ("f", ctypes.c_int)]

class XXX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

