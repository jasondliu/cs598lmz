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

assert ctypes.byref(point).contents.x == 1
assert ctypes.byref(point).contents.y == 2
# Test ctypes.c_bool
assert ctypes.c_bool(True).value == True
assert ctypes.c_bool(False).value == False
# Test ctypes.c_buffer
buf = ctypes.c_buffer("0123456789", 10)
assert buf[:] == "0123456789"
# Test ctypes.c_char
assert ctypes.c
