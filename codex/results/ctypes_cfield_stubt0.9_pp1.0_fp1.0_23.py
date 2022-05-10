import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

CStructure = ctypes.Structure
CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int)

a = S()
a.x = 1000

def f(x):
    print x.contents.x

f2 = CFuncPtr(f)
print f2
f2(ctypes.pointer(a))
