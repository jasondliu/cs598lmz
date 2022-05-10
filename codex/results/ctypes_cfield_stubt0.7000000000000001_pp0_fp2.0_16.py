import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(D.x)

ctypes.CArrayType = type(ctypes.c_int * 1)

ctypes.CPointerType = type(ctypes.POINTER(ctypes.c_int))
