import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class E(C, D):
    _fields_ = [('z', ctypes.c_int)]

class F(E):
    _fields_ = [('t', ctypes.c_int)]

class G(E):
    _fields_ = [('t', ctypes.c_int)]

class H(G):
    _fields_ = [('u', ctypes.c_int)]

class I(H):
    _fields_ = [('v', ctypes.c_int)]

class J(I):
    _fields_ = [('w', ctypes.c_int)]

class K(J):
    _fields_ = [('x', ctypes.c_int)]

class L(K):
    _fields_ = [('y', ctypes.c_int)]

class M(
