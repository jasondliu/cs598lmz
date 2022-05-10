import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(ctypes.c_int))]

class D(ctypes.Structure):
    pass

class E(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(D))]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(F))]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('ptr', ctypes.POINTER(ctypes.c_int))]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('ptr', ctypes.POINTER(I))]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes
