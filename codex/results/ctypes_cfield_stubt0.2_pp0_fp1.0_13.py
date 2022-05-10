import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(D):
    _fields_ = [('t', ctypes.c_int)]

class F(E):
    _fields_ = [('u', ctypes.c_int)]

class G(F):
    _fields_ = [('v', ctypes.c_int)]

class H(G):
    _fields_ = [('w', ctypes.c_int)]

class I(H):
    _fields_ = [('a', ctypes.c_int)]

class J(I):
    _fields_ = [('b', ctypes.c_int)]

class K(J):
    _fields_ = [('c', ctypes.c_int)]

class L(K):
    _fields_ = [('d', ctypes.c_int)]

