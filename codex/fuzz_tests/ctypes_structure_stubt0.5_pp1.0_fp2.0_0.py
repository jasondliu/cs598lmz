import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    _fields_ = [("x", ctypes.c_char)]

class C(ctypes.Structure):
    _fields_ = [("s", S),
                ("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("c2", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D)]

class F(ctypes.Structure):
    _fields_ = [("d", D)]

class G(ctypes.Structure):
    _fields_ = [("d", D),
                ("f", F)]

class H(ctypes.Structure):
    _fields_ = [("e", E),
                ("g", G)]

class I(ctypes.Structure):
    _fields_ = [("h", H),
                ("g", G)]

class J(ctypes.Structure):
    _fields_ = [
