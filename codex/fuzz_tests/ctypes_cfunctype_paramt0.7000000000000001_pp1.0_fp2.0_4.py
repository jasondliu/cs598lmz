import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

C_SQRT = FUNTYPE(1)

def c_sqrt(x):
    return C_SQRT(x)

print(c_sqrt(9.0))
 
# the same, but with a decorator
@FUNTYPE
def c_sqrt(x):
    return C_SQRT(x)

print(c_sqrt(9.0))

# another example
def f(x):
    return x**2

C_F = FUNTYPE(f)

print(C_F(2.0))

# another example
from ctypes import *
from ctypes.util import find_library

# load the library
libc = cdll.LoadLibrary(find_library('c'))

# declare the return type and argument type(s) of the function
libc.printf.restype = c_int
libc.printf.argtypes = [c_char_p,]

# call the function
libc.printf(b"Hello from
