import ctypes
# Test ctypes.CField type

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ("a",)

class Y(X):
    _fields_ = [("c", ctypes.c_int)]

class Z(X):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int)]
    _anonymous_ = ("h",)

class W(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int), ("c", ctypes.c_int)]
    _anonymous_ = ("a", "b")


