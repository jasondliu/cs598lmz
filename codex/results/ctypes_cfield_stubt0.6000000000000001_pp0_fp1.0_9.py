import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('y', C)]

class E(ctypes.Structure):
    _fields_ = [('y', D)]

class F(ctypes.Structure):
    _fields_ = [('y', E)]

class G(ctypes.Structure):
    _fields_ = [('y', F)]

class H(ctypes.Structure):
    _fields_ = [('y', G)]

class I(ctypes.Structure):
    _fields_ = [('y', H)]

class J(ctypes.Structure):
    _fields_ = [('y', I)]

class K(ctypes.Structure):
    _fields_ = [('y', J)]

class L(ctypes.Structure):
    _fields_ = [('y', K)]

class M(ctypes.Structure):
    _fields_ = [('y',
