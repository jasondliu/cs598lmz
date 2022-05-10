import ctypes
# Test ctypes.CFUNCTYPE
def func(x, y):
    return x + y

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_c = func_type(func)
print(func_c(1, 2))

# Test ctypes.POINTER
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
point = Point(1, 2)
point_p = ctypes.POINTER(Point)(point)
print(point_p.contents.x, point_p.contents.y)

# Test ctypes.byref
def func_byref(x, y):
    return x + y
func_byref_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_byref_c = func_byref_type(func_byref)
x = ctypes.
