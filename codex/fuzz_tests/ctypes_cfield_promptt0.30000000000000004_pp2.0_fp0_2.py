import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]

class U(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z),
                ("t", T)]

class V(ctypes.Structure):
    _fields_ = [("
