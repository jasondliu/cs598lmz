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
                ("f", ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [("g", ctypes.c_int),
                ("h", ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int),
                ("j", ctypes.c_int)]

class H(ctypes.Structure):
    _fields_ = [("k", ctypes.c_int),
                ("l", ctypes.c_int)]

class I(ctypes.Structure):
    _fields_ = [("m",
