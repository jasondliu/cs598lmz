import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

assert fun() == "hello"

# test with more arguments

from ctypes import *

# a function in the C library
libc = CDLL("libc.so.6")
memset = libc.memset
memset.restype = c_void_p
memset.argtypes = [c_void_p, c_int, c_size_t]

# a Python function with the same signature as the C library
def py_memset(buf, val, size):
    for i in range(size):
        buf[i] = val

# wrap the Python function with the CFUNCTYPE() factory
c_py_memset = CFUNCTYPE(c_void_p, POINTER(c_byte), c_int, c_size_t)(py_memset)

# allocate some buffer
buf = (c_byte * 100)()

# call the Python function
c_py_memset(buf, ord('x'), 100)

# call the C function
memset(buf, ord('y'),
