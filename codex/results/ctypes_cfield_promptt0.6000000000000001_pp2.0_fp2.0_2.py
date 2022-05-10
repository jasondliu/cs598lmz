import ctypes
# Test ctypes.CField

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_short),
                ("c", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("b", ctypes.c_short)]

class D(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_short),
                ("c", ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_short),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

try:
