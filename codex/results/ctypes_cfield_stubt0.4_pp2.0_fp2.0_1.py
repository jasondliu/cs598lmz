import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(D.x)
print(C.x == D.x)

print(C.x.offset)
print(D.x.offset)
print(C.x.offset == D.x.offset)

print(C.x.size)
print(D.x.size)
print(C.x.size == D.x.size)

print(C.x.name)
print(D.x.name)
print(C.x.name == D.x.name)

print(C.x.pack)
print(D.x.pack)
print(C.x.pack == D.x.pack)

print(C.x.bitsize)
print(D.x.bitsize)
print(C.x.bitsize == D.x.bitsize)

