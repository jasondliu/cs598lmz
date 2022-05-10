import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def g(x):
    return ctypes.CField(x)

def f():
    return type(ctypes.CField(1))

print(f())
print(f() is ctypes.CField)
print(f() is g(1).__class__)
