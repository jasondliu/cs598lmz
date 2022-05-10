import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1)]

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1), ("b", ctypes.c_int, 1)]

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1), ("b", ctypes.c_int, 2)]

class G(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1), ("b", ctypes.c_int, 2), ("c", ctypes.c_int, 1)]

class H(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1), ("b", ctypes.c_int, 2), ("c", ctypes.c_int, 3)]

class I(ct
