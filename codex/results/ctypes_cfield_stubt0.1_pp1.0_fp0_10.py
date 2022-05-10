import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class K(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class L
