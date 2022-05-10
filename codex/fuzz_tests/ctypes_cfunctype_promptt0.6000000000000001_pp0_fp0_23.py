import ctypes
# Test ctypes.CFUNCTYPE
def my_callback(a, b):
    return a + b
# Python 3.x only
callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
my_callback_fn = callback_type(my_callback)
my_callback_fn(1, 2)

# Test ctypes.POINTER
POINT = ctypes.c_int * 2
point = POINT(1, 2)
point
point[0]
point[1]
point.contents
point.contents.value
point.contents.value = 3
point
POINT(3, 2)

# Test ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
point = Point(1, 2)
point.x
point.y
point.x = 3
point.y = 4
point
Point(3, 4)

# Test ctypes.Union
class Point(ct
