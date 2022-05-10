import ctypes
# Test ctypes.CFUNCTYPE
# See also http://docs.python.org/library/ctypes.html#ctypes._FuncPtr
# and http://www.swig.org/Doc1.3/Python.html#Python_nn28

# Specify the return type, parameter types and calling convention.
# The calling convention is not necessary on Windows but on Linux it is necessary.
# In particular, on Linux, the default calling convention is different for Python 2 and Python 3.
# The first argument is the return type and must be specified.
# type(None) can be used to specify a void return type.
# The second argument is a tuple of the parameter types and must be specified.
# The third argument is the calling convention and is not necessary on Windows.
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Specify the default calling convention.
# On Windows, it is not necessary to specify the calling convention.
# On Linux, the default calling convention is different for Python 2 and Python 3.
# For Python 2, the default calling convention
