import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.offset)
print(C.x.size)
print(C.x.index)
print(C.x.pack)
print(C.x.ctype)
print(C.x.type)
