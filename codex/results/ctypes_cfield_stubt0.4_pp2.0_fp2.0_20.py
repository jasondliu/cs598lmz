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

class H(G):
    _fields_ = [('w', ctypes.c_int)]

class I(G):
    _fields_ = [('w', ctypes.c_int)]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class K(J):
    _fields_ = [('y', ctypes.c_int)]

class L(J):
    _fields_ = [('y', ctypes.c_int)]

class M(L):
