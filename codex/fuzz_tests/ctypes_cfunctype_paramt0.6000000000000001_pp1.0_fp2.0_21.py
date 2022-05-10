import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)

# Set up the function pointer
func = FUNTYPE(lambda x, y, z, t: x*y*z*t)

# Create the vectorized function
vec_func = vectorize_function(func)
</code>
Now you can call it like so:
<code>print vec_func(1.0, 2.0, 3.0, 4.0)
</code>

