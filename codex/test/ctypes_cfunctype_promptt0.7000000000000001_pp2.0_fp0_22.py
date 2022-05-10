import ctypes
# Test ctypes.CFUNCTYPE 
# by passing a python callback to the C library

# C prototype of callback
# int my_callback(int a, int b)

def my_callback(a, b):
    print('  called back with:', a, b)
    return a + b

# C prototype of C function using the callback
# int my_function(int a, int b, int (*cb)(int, int))

c_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(my_callback)

# load the library, using numpy routines
