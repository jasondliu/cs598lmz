import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', C)]

class E(ctypes.Structure):
    _fields_ = [('x', D)]

class F(ctypes.Structure):
    _fields_ = [('x', E)]

class G(ctypes.Structure):
    _fields_ = [('x', F)]

class H(ctypes.Structure):
    _fields_ = [('x', G)]

class I(ctypes.Structure):
    _fields_ = [('x', H)]

class J(ctypes.Structure):
    _fields_ = [('x', I)]

class K(ctypes.Structure):
    _fields_ = [('x', J)]

class L(ctypes.Structure):
    _fields_ = [('x', K)]

class M(ctypes.Structure):
    _fields_ = [('x',
