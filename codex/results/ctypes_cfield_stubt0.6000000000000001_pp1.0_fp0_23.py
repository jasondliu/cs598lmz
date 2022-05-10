import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(S2.x)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_char_p)]

print(S3.x)
print(S3.y)

S4 = type(S3)
print(S4.x)
print(S4.y)

ctypes.Structure._fields_ = [('x', ctypes.c_int)]
print(S3.x)
print(S3.y)
print(S4.x)
print(S4.y)

class S5(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    _fields_ = [('y', ctypes.c_char_p)]

print(S5.x)
print(S5.y)

ctypes.Structure._fields_ = [('x',
