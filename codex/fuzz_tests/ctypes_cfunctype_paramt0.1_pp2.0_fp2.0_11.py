import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Define the function
def f(x):
    return x**2

# Convert the function to a C function
cf = FUNTYPE(f)

# Call the C function
print cf(2)

# Define a C function
def cf2(x):
    return x**2

# Convert the C function to a Python function
f2 = FUNTYPE(cf2)

# Call the Python function
print f2(2)
</code>

