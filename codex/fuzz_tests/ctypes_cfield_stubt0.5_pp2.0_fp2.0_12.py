import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField),
                ('y', ctypes.CField)]

print(C.x.offset, C.x.size)
print(C.y.offset, C.y.size)
print(C().x, C().y)
print(C.x.__doc__)

C.x = ctypes.c_short

print(C.x.offset, C.x.size)
print(C.y.offset, C.y.size)
print(C().x, C().y)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField),
                ('y', ctypes.CField)]
print(C.x.offset, C.x.size)
print(C.y.offset, C.y.size)
print(C().x, C().y)

del C.x
print(C.x.offset, C.x.size)
print(C.y.offset, C
