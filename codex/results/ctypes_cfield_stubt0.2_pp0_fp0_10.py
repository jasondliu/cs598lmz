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

class G(F):
    _fields_ = [('w', ctypes.c_int)]

class H(G):
    _fields_ = [('v', ctypes.c_int)]

class I(H):
    _fields_ = [('u', ctypes.c_int)]

class J(I):
    _fields_ = [('t', ctypes.c_int)]

class K(J):
    _fields_ = [('s', ctypes.c_int)]

class L(K):
    _fields_ = [('r', ctypes.c_int)]

class M(L):
   
