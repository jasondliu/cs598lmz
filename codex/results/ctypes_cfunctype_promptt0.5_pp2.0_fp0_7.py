import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(2, 3)
# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def func(a, b):
    return a.contents.x + b.contents.y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int,
                           ctypes.POINTER(POINT),
                           ctypes.POINTER(POINT))

cmp_func = CMPFUNC(func)

a = POINT(1, 2)
b = POINT(3, 4)

print cmp_func(ctypes.byref(a), ctypes.byref(b))

