import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

x = fun()
print(x)

# You can also use ctypes.WINFUNCTYPE or ctypes.CFUNCTYPE for Windows and C functions respectively.

# The ctypes module provides the following functions for creating function types:

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# ctypes.WINFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False, **kwds)
# ctypes.PYFUNCTYPE(restype, *argtypes)
# ctypes.FUNCTYPE(restype, *argtypes)

# The restype and argtypes arguments are the same as for the constructor of the ctypes.CDLL class.

# The use_errno and use_last_error arguments are also the same as for the constructor of the ctypes.CDLL class.

# The **kwds argument is used to pass additional keyword arguments to the constructor of the ctypes._CFuncPtr class
