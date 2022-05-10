import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(ctypes.CField)
print(type(ctypes.CField))
print(ctypes.CField.__bases__)
