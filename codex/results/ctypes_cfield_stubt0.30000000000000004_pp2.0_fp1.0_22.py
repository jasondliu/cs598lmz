import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(D))]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(E))]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(F))]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(G))]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(H))]

class K(ctypes.Structure):
    _fields_ = [('x', ctypes
