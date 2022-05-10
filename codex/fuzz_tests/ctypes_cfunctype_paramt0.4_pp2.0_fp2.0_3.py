import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

# map the function to a C type
cfunc = FUNTYPE(func)

# call the function
cfunc(2)

# 4.0
</code>

