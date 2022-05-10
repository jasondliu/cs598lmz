import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def __init__(self):
        self.x = 42

class B(ctypes.Structure):
    _fields_ = [('a', A)]

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(A))]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(B))]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(C))]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(D))]

class G(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(E))]

class H(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(F))]

class I(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(G))
