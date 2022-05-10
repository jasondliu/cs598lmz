import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Define the C function
def my_func(x):
    return x**2

# Convert the Python function to a C function
my_cfunc = FUNTYPE(my_func)

# Call the C function
print(my_cfunc(2))

# Define a C function pointer
my_cfunc_ptr = ctypes.POINTER(FUNTYPE)

# Convert the C function to a C function pointer
my_cfunc_ptr = my_cfunc_ptr(my_cfunc)

# Call the C function pointer
print(my_cfunc_ptr.contents(2))

# Define a C function pointer
my_cfunc_ptr = ctypes.POINTER(FUNTYPE)

# Convert the Python function to a C function pointer
my_cfunc_ptr = my_cfunc_ptr(my_func)

# Call the C function pointer
print(my_cfunc_ptr.contents(2))

# Define a C function pointer
my_cfunc_ptr =
