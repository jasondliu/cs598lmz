import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    print("func", a, b)

CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func)(1, 2)

# Test ctypes.POINTER
def func(a, b):
    print("func", a, b)

POINTER(CFUNCTYPE(None, ctypes.c_int, ctypes.c_int))(func)(1, 2)

# Test ctypes.byref
def func(a, b):
    print("func", a, b)

CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func)(1, 2)

# Test ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

p = Point(1, 2)
print(p.x, p.y)

# Test ctypes.Union
class Point(ctypes.Union):
    _fields_
