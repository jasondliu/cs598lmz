import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Union):
    pass
C._fields_ = [('s', S), ('i', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('arr', C * 1), ('d', ctypes.c_double)]

print(D)
print(D().arr[0].i)
# -1
