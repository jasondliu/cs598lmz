import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]


class D(ctypes.Structure):
    _fields_ = [('y', ctypes.CField), ('x', ctypes.CField)]

print(ctypes.sizeof(C))
print(ctypes.sizeof(D))
