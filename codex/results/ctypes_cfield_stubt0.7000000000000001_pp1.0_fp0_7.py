import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CArray(ctypes.Array):
    _type_ = ctypes.CField

class C(ctypes.Structure):
    _fields_ = [('array', CArray(5))]

print(C())
