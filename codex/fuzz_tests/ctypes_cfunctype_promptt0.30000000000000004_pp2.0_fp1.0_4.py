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

point = POINT(10, 20)

point_pointer = ctypes.POINTER(POINT)

point_p = point_pointer(point)

print(point_p.contents.x)

# Test ctypes.byref
print(ctypes.byref(point))

# Test ctypes.cast
print(ctypes.cast(point_p, ctypes.c_void_p))

# Test ctypes.pointer
print(ctypes.pointer(point))

# Test ctypes.addressof
print
