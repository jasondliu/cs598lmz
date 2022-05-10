import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D)]

class F(ctypes.Structure):
    _fields_ = [("e", E)]

class G(ctypes.Structure):
    _fields_ = [("f", F)]

class H(ctypes.Structure):
    _fields_ = [("g", G)]

class I(ctypes.Structure):
    _fields_ = [("h", H)]

class J(ctypes.Structure):
    _fields_ = [("i", I)]

class K(ctypes.Structure):
    _fields_ = [("j", J)]

class L(ctypes.Structure):
    _fields_ = [("k", K)]

class M(ctypes.St
