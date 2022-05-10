import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X:
    _fields_ = [('x', ctypes.c_int)]

try:
    issubclass(ctypes.CField, ctypes.c_int)
except TypeError as e:
    print(e)

try:
    issubclass(X.x, ctypes.c_int)
except TypeError as e:
    print(e)
