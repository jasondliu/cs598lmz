import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_c = func_type(func)

print(func_c(1, 2))

# Test ctypes.POINTER
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

point_type = ctypes.POINTER(Point)
point = Point(1, 2)
point_c = point_type(point)
print(point_c.contents.x)
print(point_c.contents.y)

# Test ctypes.c_char_p
string = 'Hello, world!'
