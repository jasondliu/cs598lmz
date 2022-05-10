import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Create a C function pointer to the Python function.
f = FUNTYPE(func)

# Pass it to the C code.
lib.call_func(f)
</code>

