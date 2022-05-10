import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
def c_func(x,y):
    return x + y

# Cast Python function to C function
cfunc = FUNTYPE(c_func)

# Cast C function to Python function
pyfunc = ctypes.cast(cfunc, ctypes.py_object).value

# Call Python function
print(pyfunc(1, 2))

# Call C function
print(cfunc(1, 2))

# Call C function via Python function
print(pyfunc(1, 2))

# Call Python function via C function
print(cfunc(1, 2))
</code>

