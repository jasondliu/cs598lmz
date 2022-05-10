import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    pass

try:
    C.x = ctypes.CField(1)
except TypeError as e:
    print(e)

print('done')
