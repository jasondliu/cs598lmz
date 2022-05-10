import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(C):
    _fields_ = [('z', ctypes.c_int)]

class F(C):
    _fields_ = [('z', ctypes.c_int)]

class G(C):
    _fields_ = [('z', ctypes.c_int)]

class H(C):
    _fields_ = [('z', ctypes.c_int)]

class I(C):
    _fields_ = [('z', ctypes.c_int)]

class J(C):
    _fields_ = [('z', ctypes.c_int)]

class K(C):
    _fields_ = [('z', ctypes.c_int)]

class L(C):
    _fields_ = [('z', ctypes.c_int)]

