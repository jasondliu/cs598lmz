import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b, c):
    return a + b + c

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
print(cmp_func(1, 2, 3))

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

point = POINT(1, 2)
point_pointer = ctypes.pointer(point)
print(point_pointer.contents.x)

# Test ctypes.byref
point_pointer = ctypes.byref(point)
