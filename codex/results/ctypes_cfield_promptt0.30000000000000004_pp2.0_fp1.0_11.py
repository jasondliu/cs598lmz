import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(X):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class Z(X):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class W(Y, Z):
    _fields_ = [("e", ctypes.c_int),
                ("f", ctypes.c_int)]

# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class B(A):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class C(A):
    _fields_ = [("c", ctypes.c_int
