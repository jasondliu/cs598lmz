import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFuncPtr = type(ctypes.pythonapi.Py_InitModule4)

class C(ctypes.Structure):
    pass

C._fields_ = [('f', ctypes.CFuncPtr)]

f = C.f

print(f)
print(type(f))
print(f.__class__)

print(ctypes.CField)
print(type(f))
print(f.__class__)

print(ctypes.CFuncPtr)
print(type(f))
print(f.__class__)

print(type(f) is ctypes.CField)
print(type(f) is ctypes.CFuncPtr)

print(f.__class__ is ctypes.CField)
print(f.__class__ is ctypes.CFuncPtr)
