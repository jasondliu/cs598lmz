import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class A(ctypes.Structure):
    _fields_ = [("f", FUNTYPE), ("v", ctypes.c_int)]

def f(x):
    return x + 1

a = A(f, 1)
print a.f(1)
print a.v
</code>

