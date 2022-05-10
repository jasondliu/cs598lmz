import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(type(S.x))
print(type(ctypes.CField))
print(ctypes.CField is type(S.x))
