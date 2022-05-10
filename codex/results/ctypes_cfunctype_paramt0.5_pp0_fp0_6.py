import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Setup the wrapper function
def wrapper(f):
    def wrapper_f(x):
        return f(x)
    return FUNTYPE(wrapper_f)

# Wrap the function
wrapped_f = wrapper(f)

# Call the function
print(wrapped_f(2.0))

# Call the function with numpy arrays
print(wrapped_f(np.array(3.0)))

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# Write the function
def f(x):
    return x**2

# Import ctypes
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Setup the wrapper function
def wrapper(f):
    def wrapper_f(x):
        return f(x)
    return FUNTYPE(wrapper_f)

# Wrap the function
wrapped_f = wrapper(f)

# Call the function
print(wrapped_f(2.0))

