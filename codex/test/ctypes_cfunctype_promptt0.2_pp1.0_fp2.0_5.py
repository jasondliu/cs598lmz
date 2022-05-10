import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(1, 2))

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)

point_pointer = ctypes.POINTER(POINT)

print(point_pointer(point).contents)

# Test ctypes.byref
point_pointer = ctypes.byref(point)

