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
print(point.x, point.y)

point_pointer = ctypes.POINTER(POINT)
point_pointer_instance = point_pointer(point)
print(point_pointer_instance.contents.x, point_pointer_instance.contents.y)

# Test ctypes.byref
print(ctypes.byref(point).contents.x, ctypes.byref(point).contents.y)

# Test ctypes.string_at
print(ctypes.string_at
