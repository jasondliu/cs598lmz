import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(C):
    _fields_ = [('y', ctypes.c_int)]

class F(D, E):
    _fields_ = [('z', ctypes.c_int)]

class G(C):
    _fields_ = [('y', ctypes.c_int)]

class H(D, G):
    _fields_ = [('z', ctypes.c_int)]

class I(D, G):
    _fields_ = [('z', ctypes.c_int)]

class J(I):
    _fields_ = [('z2', ctypes.c_int)]

class K(J):
    _fields_ = [('z3', ctypes.c_int)]

class L(J):
    _fields_ = [('z3', ctypes.c_int)]


