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

class F(D):
    _fields_ = [('z', ctypes.c_int)]

class G(E, F):
    _fields_ = [('t', ctypes.c_int)]

class H(F, E):
    _fields_ = [('t', ctypes.c_int)]

class I(G, H):
    _fields_ = [('u', ctypes.c_int)]

class J(H, G):
    _fields_ = [('u', ctypes.c_int)]

class K(I, J):
    _fields_ = [('v', ctypes.c_int)]

class L(J, I):
    _fields_ = [('v', ctypes.c_int
