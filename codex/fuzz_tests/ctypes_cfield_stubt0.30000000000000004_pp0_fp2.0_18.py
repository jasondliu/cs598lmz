import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c_int))]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.CField))]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(C))]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(D))]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(E))]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(F))]

class K(ctypes.Structure):
