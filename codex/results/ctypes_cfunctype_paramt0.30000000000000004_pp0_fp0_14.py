import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x

f = FUNTYPE(myfunc)
print(f(5))

# The Python wrapper is now a function that takes an integer and returns an integer.

# The first argument to CFUNCTYPE is the return type of the function.
# The following arguments are the argument types.

# The function is now callable from C.

# The following example shows how to use a callback function.

# The callback function is called from C.
# The callback function accepts an integer and returns an integer.

# The callback function.
def myfunc(x):
    return x

# The calling function.
def call_myfunc(f, x):
    return f(x)

# The C function.
libc = ctypes.CDLL(None)
libc.call_myfunc.argtypes = (FUNTYPE, ctypes.c_int)
libc.call_myfunc.restype = ctypes.c_int

# The Python wrapper.
def call
