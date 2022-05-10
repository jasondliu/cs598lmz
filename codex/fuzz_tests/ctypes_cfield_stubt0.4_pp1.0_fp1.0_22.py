import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class D(C):
    _fields_ = [('x', ctypes.c_int)]

class E(C):
    _fields_ = [('x', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class G(F):
    _fields_ = [('x', ctypes.c_int)]

class H(F):
    _fields_ = [('x', ctypes.c_int)]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class J(I):
    _fields_ = [('y', ctypes.c_int)]

class K(I):
    _fields_ = [('y', ctypes.c_int)]

class L(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int
