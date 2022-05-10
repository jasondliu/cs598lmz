import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("e", ctypes.c_int),
                ("d", D)]

class F(ctypes.Structure):
    _fields_ = [("e", ctypes.c_int),
                ("d", D),
                ("f", ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [("e", ctypes.c_int),
                ("d", D),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int)]

class H(ctypes.Structure):
    _fields_ = [("e", ctypes.c_int),
                ("d", D),
                ("f",
