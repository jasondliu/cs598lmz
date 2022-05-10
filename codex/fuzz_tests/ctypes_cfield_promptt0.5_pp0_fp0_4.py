import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("e", ctypes.c_int),
                ("f", ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int)]

class C(ctypes.Structure):
