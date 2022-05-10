import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(f(1, 2))

# Test ctypes.POINTER

class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

p = POINT(1, 2)
pp = ctypes.POINTER(POINT)(p)
print(pp.contents.x, pp.contents.y)

# Test ctypes.byref

def func2(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))(func2)
a = ctypes.c_int(1)
b = ctypes.c_int(2)
