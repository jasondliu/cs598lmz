import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFUNC(func)

assert cfunc(2, 3) == 5
# Test ctypes.byref

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = Point(1, 2)

