import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b, c):
    return a + b + c

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
print cmp_func(1, 2, 3)

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
point_t = POINT * 5
point = point_t()
point[0].x = 1
point[0].y = 2
point[1].x = 3
point[1].y = 4
point[2].x = 5
point[2].y = 6
point[3].x = 7
point[3].y = 8
point[4].x = 9
point[4].y = 10

print point[0].x, point[0].y
print point[1].x, point[1
