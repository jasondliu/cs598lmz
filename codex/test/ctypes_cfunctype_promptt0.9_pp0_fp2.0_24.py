import ctypes
# Test ctypes.CFUNCTYPE

#################################################################

# define int func(int)
FUNC_INT_INT = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call func(3) == 6
def func(x):
    return x+3

# test a C function: get its address and coerce it to a python object
