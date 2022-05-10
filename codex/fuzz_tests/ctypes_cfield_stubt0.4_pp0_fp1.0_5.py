import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    pass

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class G(ctypes.Structure):
    pass

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class I(ctypes.Structure):
    pass

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class K(ctypes.Structure):
    pass

class L(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class M(ctypes.Structure):
    pass

class N(ctypes.Structure):
    _fields_ = [
