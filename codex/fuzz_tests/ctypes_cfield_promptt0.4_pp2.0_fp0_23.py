import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(X):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class Z(Y):
    _fields_ = [("e", ctypes.c_int),
                ("f", ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class B(A):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class C(B):
    _fields_ = [("e", ctypes.c_int),
                ("f", ctypes.c_int)]

class D(C):
    _fields_ = [("g", ctypes.c_int),
                ("h", ctypes.
