import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Define the function to be called
def myfunc(x):
    return 2 * x

# Convert the function to a C pointer
myfunc_c = FUNTYPE(myfunc)

# Call the function via the pointer
print(myfunc_c(2))

# Define the function to be called
def myfunc(x):
    return 2 * x

# Convert the function to a C pointer
myfunc_c = FUNTYPE(myfunc)

# Call the function via the pointer
print(myfunc_c(2))

# Define the function to be called
def myfunc(x):
    return 2 * x

# Convert the function to a C pointer
myfunc_c = FUNTYPE(myfunc)

# Call the function via the pointer
print(myfunc_c(2))

# Define the function to be called
def myfunc(x):
    return 2 * x

# Convert the function to a C pointer
myfunc_c = FUNTYPE(myfunc)

# Call
