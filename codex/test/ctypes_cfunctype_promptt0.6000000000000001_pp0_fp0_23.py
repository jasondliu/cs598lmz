import ctypes
# Test ctypes.CFUNCTYPE
def my_callback(a, b):
    return a + b
# Python 3.x only
callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
my_callback_fn = callback_type(my_callback)
my_callback_fn(1, 2)

# Test ctypes.POINTER
POINT = ctypes.c_int * 2
point = POINT(1, 2)
point
point[0]
point[1]
