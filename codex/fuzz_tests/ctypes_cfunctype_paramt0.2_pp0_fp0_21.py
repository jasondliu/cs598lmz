import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

#%%

# Ctypes

import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL('./libmylib.so')

# Set the return type of the C function
lib.mylib_func.restype = ctypes.c_double

# Call the C function
print(lib.mylib_func(2))

#%%

# Ctypes

import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL('./libmylib.so')

# Set the return type of the C function
lib.mylib_func.restype = ctypes.c_double

# Call the C function
print(lib.mylib_func(2))

#%%

# Ctypes

import ctypes

# Load the shared library into ctypes
lib = ctypes.CD
