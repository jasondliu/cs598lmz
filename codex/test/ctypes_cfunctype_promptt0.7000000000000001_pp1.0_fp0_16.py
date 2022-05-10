import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x + 42

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
print(cfunc(5))

# Test ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

point = Point(5, 42)
print(point.x, point.y)

# Test ctypes.cast
