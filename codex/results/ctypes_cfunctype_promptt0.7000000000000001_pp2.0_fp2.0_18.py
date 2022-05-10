import ctypes
# Test ctypes.CFUNCTYPE
def func(arg):
    print(arg)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)
print(cmp_func)

class POINT(ctypes.Structure):
    _fields_ = ("x", ctypes.c_int), ("y", ctypes.c_int)

PointType = POINT

# Test ctypes.POINTER
Point = PointType
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)

pp = ctypes.POINTER(PointType)
print(pp)

# Test ctypes.WINFUNCTYPE
WINFUNCTYPE = ctypes.WINFUNCTYPE
print(WINFUNCTYPE)

# Test ctypes.c_ssize_t
print(ctypes.c_ssize_t)

# Test ctypes.c_wchar_p
print(ctypes.c_wchar_p)
