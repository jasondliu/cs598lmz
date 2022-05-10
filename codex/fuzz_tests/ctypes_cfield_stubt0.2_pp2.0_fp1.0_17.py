import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class F(E):
    _fields_ = [('z', ctypes.c_int)]

class G(E):
    _fields_ = [('z', ctypes.c_int)]

class H(E):
    _fields_ = [('z', ctypes.c_int)]

class I(E):
    _fields_ = [('z', ctypes.c_int)]

class J(E):
    _fields_ = [('z', ctypes.c_int)]

class K(E):
    _fields_ = [('z', ctypes.c_int)]

class L(E):
    _fields_ = [('z', ctypes
