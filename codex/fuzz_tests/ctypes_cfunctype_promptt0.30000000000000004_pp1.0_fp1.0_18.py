import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CFUNCTYPE(c_int, c_int, c_int)(func)

# Test ctypes.PYFUNCTYPE
def func(a, b):
    return a + b

PYFUNCTYPE(c_int, c_int, c_int)(func)

# Test ctypes.WINFUNCTYPE
def func(a, b):
    return a + b

WINFUNCTYPE(c_int, c_int, c_int)(func)

# Test ctypes.Structure
class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

POINT(10, 20)

# Test ctypes.Union
class POINT(Union):
    _fields_ = [("x", c_int),
                ("y", c_int)]

POINT(10)

# Test ctypes.Array
class POINT(Structure):
    _fields_ = [("x", c
