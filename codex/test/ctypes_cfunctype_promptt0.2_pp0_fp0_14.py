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

point = Point(1, 2)
point_pointer = ctypes.pointer(point)
print(point_pointer.contents.x)

# Test ctypes.byref
point_byref = ctypes.byref(point)
