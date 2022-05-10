import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_c = func_type(func)
func_c(1, 2)

# Test ctypes.POINTER
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point_type = ctypes.POINTER(Point)
point = Point(1, 2)
point_c = point_type(point)
point_c.contents.x

# Test ctypes.c_void_p
