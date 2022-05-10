import ctypes
# Test ctypes.CField

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("b", ctypes.CField)]

class C(ctypes.Structure):
    _fields_ = [("c", B)]

class D(ctypes.Structure):
    _fields_ = [("d", C)]

class E(ctypes.Structure):
    _fields_ = [("e", D)]

class F(ctypes.Structure):
    _fields_ = [("f", E)]

class G(ctypes.Structure):
    _fields_ = [("g", F)]

class H(ctypes.Structure):
    _fields_ = [("h", G)]

class I(ctypes.Structure):
    _fields_ = [("i", H)]

class J(ctypes.Structure):
    _fields_ = [("j", I)]

class K(ctypes.Structure):
    _fields_ =
