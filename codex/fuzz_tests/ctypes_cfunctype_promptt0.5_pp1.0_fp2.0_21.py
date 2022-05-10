import ctypes
# Test ctypes.CFUNCTYPE

# Import the module
import sys
sys.path.append('..')
from sample import *

# Call the function
r = add_arrayi([1, 2, 3, 4], 4)
if r != 10:
    raise RuntimeError("Bad result from add_arrayi")

# Define a ctypes callback function type
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Define a python function to pass as the callback
def py_add_one(x):
    return x + 1

# Call the function
r = add_one_callback(py_add_one, 5)
if r != 6:
    raise RuntimeError("Bad result from add_one_callback")
