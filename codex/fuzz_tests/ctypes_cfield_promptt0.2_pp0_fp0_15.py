import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

class W(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

class V(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

class U(ct
