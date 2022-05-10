import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    print a, b
cfunc = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func)
cfunc(1, 2)

# Test ctypes.POINTER
c_int_p = ctypes.POINTER(ctypes.c_int)
i = ctypes.c_int(42)
p = ctypes.pointer(i)
assert ctypes.addressof(p.contents) == ctypes.addressof(i)
assert p.contents.value == 42

# Test ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
pt = Point(1, 2)
assert pt.x == 1
assert pt.y == 2

# Test ctypes.Union
class Point(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
