import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a * b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(2, 3))

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

point = POINT(10, 20)
print(point.x, point.y)

POINT_P = ctypes.POINTER(POINT)
point_p = POINT_P(point)
print(point_p.contents.x, point_p.contents.y)

# Test ctypes.byref
point.x = 30
point.y = 40
print(point_p.contents.x, point_p.contents.y)

# Test ctypes.string_at
s = ctypes.string
