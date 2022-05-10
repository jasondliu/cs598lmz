import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
cos = FUNTYPE(lib.cos)
cos(1)

#%%
import ctypes
import numpy as np

# Load the library using 
lib = ctypes.cdll.LoadLibrary('./libmylib.so')

# Define the return type and argument type for the function
# in this case we are looking at cos(double)
lib.cos.restype = ctypes.c_double
lib.cos.argtypes = [ctypes.c_double]

# Create a python function that calls the cos function in the library
# This is equivalent to cos(x) in C
pycos = lib.cos

# We can now use the function like any other function
print(pycos(1))

# Create a numpy array
x = np.linspace(0, 1, 10, dtype=np.float64)
print(x)

# Use the python cos function to evaluate the cos of the numpy array
print(pycos(x))

#%%
import ctypes

# Load
