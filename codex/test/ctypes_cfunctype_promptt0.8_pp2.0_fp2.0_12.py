import ctypes
# Test ctypes.CFUNCTYPE using a function that takes a file argument

# This function takes an open file and reads it.
def readsomefile(f):
    assert(f)
    x = f.read()
    assert(type(x) == str)
    return len(x)

# Declare some functions
my_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(readsomefile)

filep = ctypes.c_void_p()
