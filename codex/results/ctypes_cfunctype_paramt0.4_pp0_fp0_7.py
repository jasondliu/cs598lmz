import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Define the function.
def f(x):
    return x**2

# Convert to ctypes.
f_ctypes = FUNTYPE(f)

# Call the function.
f_ctypes(2)
</code>

