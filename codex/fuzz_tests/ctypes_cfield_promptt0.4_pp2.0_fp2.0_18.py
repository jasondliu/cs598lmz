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
    _fields_ = [("d", D),
                ("e", E)]

class G(ctypes.Structure):
    _fields_ = [("f", ctypes.POINTER(F))]

class H(ctypes.Structure):
    _fields_ = [("f", F)]

class I(ctypes.Structure):
    _fields_ = [("f", ctypes.POINTER(F)),
                ("g", G)]

class J(ctypes.Structure):
    _fields_ = [("f", ctypes.POINTER(
