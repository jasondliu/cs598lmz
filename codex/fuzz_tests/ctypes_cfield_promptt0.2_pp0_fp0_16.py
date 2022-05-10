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

class A(ctypes.Structure):
    _fields_ = [("z", Z),
                ("e", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("f", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("b", B),
                ("g", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("h", ctypes.c_int)]

