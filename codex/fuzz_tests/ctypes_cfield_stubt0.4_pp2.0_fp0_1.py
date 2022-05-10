import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(C):
    _fields_ = [('y', ctypes.c_int)]

class F(D):
    _fields_ = [('y', ctypes.c_int)]

class G(E):
    _fields_ = [('z', ctypes.c_int)]

class H(F):
    _fields_ = [('z', ctypes.c_int)]

class I(G):
    _fields_ = [('w', ctypes.c_int)]

class J(H):
    _fields_ = [('w', ctypes.c_int)]

class K(I):
    _fields_ = [('v', ctypes.c_int)]

class L(J):
    _fields_ = [('v', ctypes.c_int)]

class M(K):
