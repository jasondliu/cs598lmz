import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def _my_sin(x):
    return np.sin(x)

# Wrap it into a C function pointer
CFUNC = FUNTYPE(_my_sin)

# Create an array of function pointers
sines = np.empty(10, dtype=FUNTYPE)
sines[:] = CFUNC

# The first element is now a C function pointer.
# Use it to evaluate the sine at 0.5
print sines[0](0.5)
</code>

<code>&gt;&gt;&gt; print sines[0](0.5)
0.479425538604
</code>

