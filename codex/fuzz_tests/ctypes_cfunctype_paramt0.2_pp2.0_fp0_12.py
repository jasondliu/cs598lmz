import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

#%%

# Using ctypes to call a C function

import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL('./libfunctions.so')

# Set the return type of the function
lib.f.restype = ctypes.c_double

# Set the argument type of the function
lib.f.argtypes = [ctypes.c_double]

print(lib.f(2))

#%%

# Using ctypes to call a C function

import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL('./libfunctions.so')

# Set the return type of the function
lib.f.restype = ctypes.c_double

# Set the argument type of the function
lib.f.argtypes = [ctypes.c_double]

print
