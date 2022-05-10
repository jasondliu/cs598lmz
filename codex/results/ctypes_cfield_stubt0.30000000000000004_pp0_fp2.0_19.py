import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', C)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(C))]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.CField))]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c_int))]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.POINTER(ctypes.c_int)))]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.POINTER(ctypes.CField)))]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.PO
