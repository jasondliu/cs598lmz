import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

MyType = ctypes.CField

print(ctypes.sizeof(ctypes.c_int))
s = S()
print(s.x)
