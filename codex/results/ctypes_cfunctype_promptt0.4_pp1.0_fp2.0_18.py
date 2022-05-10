import ctypes
# Test ctypes.CFUNCTYPE
def py_callback(a, b):
    print(a, b)
    return a + b

c_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(py_callback)

print(c_callback(1, 2))

# Test ctypes.POINTER
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

point = Point(1, 2)
print(point.x, point.y)

c_point = ctypes.POINTER(Point)(point)
print(c_point.contents.x, c_point.contents.y)

# Test ctypes.byref
def py_callback2(a, b):
    print(a, b)
    return a + b

c_callback2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(py_callback2
