import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(C):
    _fields_ = [('z', ctypes.c_int),
                ('w', ctypes.c_int)]

class F(D):
    _fields_ = [('w', ctypes.c_int),
                ('v', ctypes.c_int)]

class G(F):
    _fields_ = [('u', ctypes.c_int)]

class H(E):
    _fields_ = [('v', ctypes.c_int)]

class I(H):
    _fields_ = [('u', ctypes.c_int)]

class J(I):
    _fields_ = [('t', ctypes.c_int)]

class K(J):
    _fields_ = [('s', ctypes.c_int
