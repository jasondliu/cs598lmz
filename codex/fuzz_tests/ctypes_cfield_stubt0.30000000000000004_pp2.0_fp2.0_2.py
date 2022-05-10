import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int)]

print(C.x)
print(C.y)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int), ('z', ctypes.c_int)]

print(C.x)
print(C.y)
print(C.z)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int), ('z', ctypes.c_int), ('w', ctypes.c_int)]

print(C.x)
print(C.y)
print(C.z)
print(C.w)

class C(ctypes.Structure):
   
