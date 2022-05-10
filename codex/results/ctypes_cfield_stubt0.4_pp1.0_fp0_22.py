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

class G(D):
    _fields_ = [('z', ctypes.c_int)]

class H(D):
    _fields_ = [('z', ctypes.c_int)]

class I(D):
    _fields_ = [('z', ctypes.c_int)]

class J(D):
    _fields_ = [('z', ctypes.c_int)]

class K(D):
    _fields_ = [('z', ctypes.c_int)]

class L(D):
    _fields_ = [('z', ctypes.c_int)]

class M(D):
    _fields
