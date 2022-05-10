import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(type(S.x))
print(isinstance(S.x, type(ctypes.c_int)))
print(isinstance(S.x, ctypes.CField))
