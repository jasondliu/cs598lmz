import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int64, # Return value is a 64-bit int
                    ctypes.c_int64,   # x is an int
                    ctypes.c_int64)   # y is an int

# Set the Python callback.
@FUNTYPE
def my_fun(x, y):
    print("Python callback says " \
          "C++ program raised {0} to the power of {1}.".format(x, y))
    return 0

clib.fun(my_fun)
 
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int64, # Return value is a 64-bit int
                    ctypes.c_int64,   # x is an int
                    ctypes.c_int64)   # y is an int

# Set the Python callback.
@FUNTYPE
def my_fun(x, y):
    z = x**y
    print("Python callback:")
    print("\t{0} raised to the power of {1} = {2}".format(x, y, z))
