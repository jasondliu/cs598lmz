import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

# Define a python function
def exponential(x, y):
    return x * y

# Convert the python function to a c function
cfunc = FUNTYPE(exponential)

# Call the c function
print(cfunc(1, 2))

# Call the python function
print(exponential(1, 2))
</code>
Output:
<code>2.0
2
</code>

