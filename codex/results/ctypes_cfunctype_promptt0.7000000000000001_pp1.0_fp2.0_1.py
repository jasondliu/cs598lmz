import ctypes
# Test ctypes.CFUNCTYPE to go from Python to C and back
from ctypes import CFUNCTYPE, c_int, c_float

# Define a C function that takes a float and an int, and returns a float
@CFUNCTYPE(c_float, c_float, c_int)
def c_func(x, n):
    return x**n

# Call the C function with integer arguments
c_func(1., 5)

# Call the C function with float arguments
c_func(2.5, 3)
 
# Define a function that takes a float and an int, and returns a float
def py_func(x, n):
    return x**n

# Call the function with integer arguments
py_func(1., 5)

# Call the function with float arguments
py_func(2.5, 3)

# Call the C function with integer arguments from Python
c_func(1, 5)

# Call the C function with float arguments from Python
c_func(2.5, 3)

# Call the C function with integer arguments from Python
py_
