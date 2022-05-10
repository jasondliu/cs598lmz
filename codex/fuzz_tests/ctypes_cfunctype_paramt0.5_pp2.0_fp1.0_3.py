import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

cfunc = FUNTYPE(f)

print(cfunc(3))

# Note that the function is now a ctypes function, and not a Python function.
print(type(cfunc))
print(type(f))

# Note that you can also pass a ctypes function to Python.
def c_f(x):
    return x**2

c_cfunc = FUNTYPE(c_f)
print(c_cfunc(3))

# You can also use the ctypes library to call C functions directly.
# For example, we can call the C sqrt function in the standard math library
# by using ctypes.cdll.LoadLibrary to load the library, and then using
# its .sqrt method.

# Load the C math library
libc = ctypes.cdll.LoadLibrary('libc.so.6')

# Tell ctypes that the libc.sqrt function should take a ctypes.c_double,
# and return a
