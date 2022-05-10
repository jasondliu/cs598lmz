import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class B(A):
    _fields_ = [("a", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

# Test ctypes.CArray
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int * 5)]

class D(C):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("d", ctypes.c_int * 5),
                ("e", ctypes.c_int)]

# Test ctypes.CArray + ctypes.CField
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("
