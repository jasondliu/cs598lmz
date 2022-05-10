import ctypes
ctypes.cast(0, ctypes.py_object)

# Function to be called from C
def py_func(x):
    return x + 1

# Convert the Python function into a C function
C_func = ctypes.CFUNCTYPE(ctypes.c_int)(py_func)

# Call the C function
print(C_func(1))

# Convert the Python function into a C function
C_func = ctypes.CFUNCTYPE(ctypes.py_object)(py_func)

# Call the C function
print(C_func(1))

# Convert the Python function into a C function
C_func = ctypes.CFUNCTYPE(ctypes.py_object)(py_func)

# Call the C function
print(C_func(1))

# Convert the Python function into a C function
C_func = ctypes.CFUNCTYPE(ctypes.py_object)(py_func)

# Call the C function
print(C_func(1))

# Convert the Python function into a C function
C_func
