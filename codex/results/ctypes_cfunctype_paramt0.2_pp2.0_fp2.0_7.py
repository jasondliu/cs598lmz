import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

#%%

import ctypes
import numpy as np

# Define the return type and argument types
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Define the function in C
c_code = """
double f(double x){
    return x*x;
}
"""

# Compile the C code
lib = ctypes.CDLL(None)
lib.f.restype = ctypes.c_double
lib.f.argtypes = [ctypes.c_double]
lib.f.__doc__ = c_code
lib.f.__name__ = "f"

# Create a Python function
f = FUNTYPE(lib.f)

# Test the function
print(f(2))

#%%

import ctypes
import numpy as np

#
