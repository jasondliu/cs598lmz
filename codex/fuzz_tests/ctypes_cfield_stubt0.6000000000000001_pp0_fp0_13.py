import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    pass

C.__dict__['a'] = ctypes.CField(ctypes.c_int, None, None)
C.__dict__['b'] = ctypes.CField(ctypes.c_int, None, None)

def foo():
    C.a = 1
    C.b = 2
    return C.a, C.b

print foo()
