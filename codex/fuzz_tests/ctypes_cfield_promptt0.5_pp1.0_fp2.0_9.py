import ctypes
# Test ctypes.CField

lib = ctypes.CDLL(ctypes.util.find_library("c"))

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["a"]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["a"]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["a"]

class A(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]
    _anonymous_ = ["x", "y"]

class B(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z",
