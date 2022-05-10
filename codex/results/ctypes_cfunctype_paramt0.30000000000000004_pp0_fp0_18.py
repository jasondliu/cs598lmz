import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The Python function
def myfunc(a, b):
    return a + b

# Wrap the Python function
cfunc = FUNTYPE(myfunc)

# Call the C function
print(cfunc(1, 2))
</code>

