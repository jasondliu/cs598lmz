import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(C))]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(D))]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(E))]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(F))]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(G))]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(H))]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(I))]

class K(ctypes.Structure):
    _fields_ =
