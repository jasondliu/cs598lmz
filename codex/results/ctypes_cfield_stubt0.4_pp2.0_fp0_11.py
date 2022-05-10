import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

class F(object):
    def __init__(self, x):
        self.x = x

class G(F, ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class H(F, ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class I(H, ctypes.Structure):
    _fields_ = [('z', ctypes.c_int)]

class J(G, I):
    _fields_ = [('w', ctypes.c_int)]

class K(G, I):
    _fields_ = [('w', ctypes.c_int)]

class L(G, I):
    _
