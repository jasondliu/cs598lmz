import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# This one is called by the C code
@CFUNCTYPE(c_int, c_int, c_int)
def add(a, b):
    return a + b

# This one is called by the C code
@CFUNCTYPE(c_int, c_int, c_int)
def sub(a, b):
    return a - b

# This one is called by the C code
@CFUNCTYPE(c_int, c_int, c_int)
def mul(a, b):
    return a * b

# This one is called by the C code
@CFUNCTYPE(c_int, c_int, c_int)
def div(a, b):
    return a / b

# This one is called by the C code
@CFUNCTYPE(c_int, c_int, c_int)
def mod(a, b):
    return a % b

# This one is called
