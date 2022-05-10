import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Y(X):
    _fields_ = [("c", ctypes.c_int)]

class Z(Y):
    _fields_ = [("d", ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [("x", X), ("y", ctypes.c_int)]

class B(A):
    _fields_ = [("z", ctypes.c_int)]

class C(B):
    _fields_ = [("w", ctypes.c_int)]

class D(X):
    _fields_ = [("c", ctypes.c_int)]

class E(D):
    pass

class F(A):
    _fields_ = [("y", ctypes.c_int)]

class G(A):
    _fields_ = [("y", ctypes.c_int), ("z", ctypes.c
