import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

import ctypes
import ctypes.util

# Load the library
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Define the function prototype
prototype = FUNTYPE(ctypes.c_int, ctypes.c_int)

# Bind the function to the prototype
paramflags = (1, "x"), (1, "y")
libc.add.argtypes = [ctypes.c_int, ctypes.c_int]
libc.add.restype = ctypes.c_int

# Define a function that matches the prototype
def py_add(x, y):
    return x + y

# Convert the Python function to a C function
c_add = prototype(py_add)

# Call the C function via the prototype
print c_add(1, 2)

# Call the C function directly
print libc.add(1, 2)
</code>

