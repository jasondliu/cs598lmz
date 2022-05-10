import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Here we have a python function that returns an int
# We can use ctypes to convert it to a C-compatible function
def myfunc(x):
    return x * x * x * x

# Here is a C function that takes a C function and calls it
c_lib.call_c_function(FUNTYPE(myfunc))
</code>

