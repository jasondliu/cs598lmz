import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    _fields_ = [("x", x), ("x", x)]

class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char_p), ("x", ctypes.c_char_p)]

class B(ctypes.Structure):
    x = ctypes.c_char_p
    _fields_ = [("x", x), ("x", x)]

class C(ctypes.Structure):
    x = ctypes.c_char_p
    _anonymous_ = ["x"]
    _fields_ = [("x", x), ("x", x)]

class D(ctypes.Structure):
    _anonymous_ = ["x"]
    _fields_ = [("x", ctypes.c_char_p), ("x", ctypes.c_char_p)]

class E(ctypes.Structure):
    x = ctypes.c_char_p
    _anonymous_ = ["x"]
    _fields_ = [("x", x), ("
