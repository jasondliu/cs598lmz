import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int),
                ("w", ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int),
                ("w", ctypes.c_int),
                ("v
