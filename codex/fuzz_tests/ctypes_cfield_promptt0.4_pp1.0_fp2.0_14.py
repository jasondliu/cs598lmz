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

class A(ctypes.Structure):
    _fields_ = [("z", Z),
                ("a", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("z", Z),
                ("b", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("a", A),
                ("b", B),
                ("c", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int
