import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return sin(x)

f_cfunc = FUNTYPE(f)

# Call the C function
print f_cfunc(1.0)

# Call the Python function
print f(1.0)

# Call the C function through the Python function
print f.__call__(1.0)

# Call the C function through the C function pointer
print ctypes.cast(f, FUNTYPE).__call__(1.0)

# Call the Python function through the C function pointer
print ctypes.cast(f_cfunc, FUNTYPE).__call__(1.0)
</code>
Here's the output:
<code>0.841470984808
0.841470984808
0.841470984808
0.841470984808
0.841470984808
</code>

