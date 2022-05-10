import ctypes
# Test ctypes.CFUNCTYPE for functions that return void.

from ctypes import *

TestError = "TestError"

class X(Structure):
    pass
X._fields_ = [("a", c_int)]

p = pointer(X())

dll = CDLL(ctypes.util.find_library("c"))

c_sin = dll.sin
c_sin.restype = c_double
c_sin.argtypes = [c_double]

c_printf = dll.printf
c_printf.argtypes = [c_char_p]
c_printf.restype = c_int

c_puts = dll.puts
c_puts.argtypes = [c_char_p]
c_puts.restype = c_int

c_raise = dll.raise
c_raise.argtypes = [c_int]
c_raise.restype = None

# this works for both _synchronous_ and asynchronous exceptions
def raises_exception(func, *args):
    try:
        func(*args)
    except
