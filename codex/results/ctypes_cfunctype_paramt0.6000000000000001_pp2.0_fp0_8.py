import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)

print(f(2))

# By default, the arguments and return type are assumed to be C int.
# If you want to use another type, you must declare it explicitly.

# The ctypes module provides a number of functions for working with C data types in Python.
# The c_double data type is one of these. It represents the C double data type.
# You can find a list of the available data types in the ctypes documentation.

# The ctypes module also provides the CFUNCTYPE() function, which takes the return type and the types of the parameters of the C function as arguments and returns a Python object that represents the C function.

# The CFUNCTYPE() function returns a Python object that represents the C function.
# The ctypes module provides a number of functions that can be used to call C functions using this object.
# The simplest of these is the __call__() method, which we used in the example above.
# You can also
