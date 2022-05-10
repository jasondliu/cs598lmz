import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(ctypes.CField)
print(ctypes.CField.__module__)

class C(ctypes.Structure):
    pass

ctypes.CStruct = type(C)
print(ctypes.CStruct)
print(ctypes.CStruct.__module__)

class D(ctypes.Union):
    pass

ctypes.CUnion = type(D)
print(ctypes.CUnion)
print(ctypes.CUnion.__module__)

ctypes.CArray = type(S.x[:])
print(ctypes.CArray)
print(ctypes.CArray.__module__)
