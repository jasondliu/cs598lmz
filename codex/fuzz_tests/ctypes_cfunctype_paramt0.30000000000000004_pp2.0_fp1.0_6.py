import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create a function that takes two integers and returns their sum
def add(a, b):
    return a + b

# Convert the Python function to a C function
cfunc = FUNTYPE(add)

# Call the C function
print(cfunc(1, 2))

# Create a C function pointer from the Python function
cfunc_ptr = ctypes.cast(cfunc, ctypes.c_void_p).value

# Call the C function pointer
print(ctypes.pythonapi.PyCapsule_GetPointer(cfunc_ptr, None))
</code>

