import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(S.x)
print(ctypes.CField)
print(isinstance(S.x, ctypes.CField))
