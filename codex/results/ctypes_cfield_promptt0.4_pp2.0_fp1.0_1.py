import ctypes
# Test ctypes.CField.from_param

import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

class A(ctypes.Structure):
    _fields_ = [("z", Z)]

class B(ctypes.Structure):
    _fields_ = [("a", A)]

class C(ctypes.Structure):
    _fields_ = [("b", B)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D)]

class F(ctypes.Structure):
    _fields_ = [("e", E)]

class G(ctypes.Structure):
    _fields_ = [("f", F)]

class H(ctypes.St
