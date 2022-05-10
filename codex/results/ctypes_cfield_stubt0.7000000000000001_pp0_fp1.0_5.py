import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def f(x):
    x.value = 3

f.restype = ctypes.CField
f.argtypes = [ctypes.CField]
f(S.x)
print S.x.value
