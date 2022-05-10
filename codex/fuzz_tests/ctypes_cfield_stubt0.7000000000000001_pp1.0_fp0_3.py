import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class M(type):
    pass

class C(metaclass=M):
    pass

class D(C):
    pass

class A(ctypes.Structure):
    _fields_ = [("next", ctypes.POINTER(A))]

class B(ctypes.Structure):
    _fields_ = [("next", ctypes.POINTER(A))]

class E(ctypes.CField):
    pass

class F(ctypes.Array):
    pass

class G(A):
    pass

class H(A):
    pass

import _ctypes_test

class I(ctypes.Structure):
    pass

class J(ctypes.Union):
    pass

class K(ctypes.Union):
    pass
