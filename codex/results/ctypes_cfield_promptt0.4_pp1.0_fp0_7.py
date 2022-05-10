import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b",)

class Y(X):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Z(X):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b",)

class W(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class V(W):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b",)

class U(W):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int
