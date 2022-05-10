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

class F(E):
    _fields_ = [('z', ctypes.c_int)]

class G(E):
    _fields_ = [('z', ctypes.c_int)]

class H(F, G):
    _fields_ = [('w', ctypes.c_int)]

class I(H):
    _fields_ = [('w', ctypes.c_int)]

class J(I):
    _fields_ = [('w', ctypes.c_int)]

class K(J):
    _fields_ = [('w', ctypes.c_int)]

class L(K):
    _fields_ = [('w', ctypes.c_int)]

class M(L):
   
