import ctypes
# Test ctypes.CFUNCTYPE
def foo(a, b):
    return a + b

foo_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(foo)
print(foo_c(1, 2))

# Test ctypes.POINTER
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = Point(1, 2)
p_p = ctypes.POINTER(Point)(p)
print(p_p.contents.x)
print(p_p.contents.y)

# Test ctypes.byref
p_p = ctypes.byref(p)
