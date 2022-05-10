import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y)]

class A(ctypes.Structure):
    _fields_ = [("z", Z)]

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("b", B),
                ("c", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

class E(ctypes.Structure):
   
