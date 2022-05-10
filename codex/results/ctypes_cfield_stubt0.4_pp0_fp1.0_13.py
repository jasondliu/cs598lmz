import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    pass

class E(C):
    _fields_ = [('y', ctypes.c_int)]

class F(E):
    pass

class G(E):
    _fields_ = [('z', ctypes.c_int)]

class H(G):
    pass

class I(G):
    _fields_ = [('z', ctypes.c_double)]

class J(G):
    _fields_ = [('z', ctypes.c_double), ('w', ctypes.c_int)]

class K(J):
    pass

class L(J):
    _fields_ = [('w', ctypes.c_int)]

class M(L):
    pass

class N(L):
    _fields_ = [('w', ctypes.c_double)]

class O(L):
    _fields_ = [('w', ctypes.c_double
