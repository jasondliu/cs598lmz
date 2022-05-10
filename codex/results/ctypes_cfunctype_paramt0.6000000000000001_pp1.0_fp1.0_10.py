import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Wrapper for the C function.
def func(x, y):
    return x + y

# Get a pointer to the function.
fptr = FUNTYPE(func)

# Now call the function via the pointer.
print(fptr(5, 8))
</code>

