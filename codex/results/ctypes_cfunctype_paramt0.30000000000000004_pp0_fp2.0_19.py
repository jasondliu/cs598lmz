import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The C function we want to call
def my_function(x):
    print("You passed {}".format(x))
    return x

# Convert the Python function into a C function
cfunc = FUNTYPE(my_function)

# Call the C function
cfunc(42)

# Call the C function through a Python function
def py_function(x):
    return cfunc(x)

py_function(42)
</code>

