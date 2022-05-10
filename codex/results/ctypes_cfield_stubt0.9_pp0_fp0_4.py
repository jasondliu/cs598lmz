import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.POINTER(ctypes.c_double)),
                ("y", ctypes.POINTER(ctypes.c_double))]

s = S()
print dir(s.x)
print dir(s.y)

s = S.in_dll(ctypes.CDLL("_ctypes_test.so"), "s")
x = s.contents.x
y = s.contents.y
print dir(x)
print dir(y)
