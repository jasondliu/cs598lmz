import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

my_callback_c(1, 2)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: The result type of the callback.
# argtypes: A sequence specifying the argument types of the callback.
# use_errno: If True, the callback function will have an extra keyword argument called errno.
# use_last_error: If True, the callback function will have an extra keyword argument called last_error.

# The callback function must return an integer value.
# If the callback function returns a negative integer, the calling function will raise an exception.
# If the callback function returns a positive integer, the calling function will not raise an exception.
# If the callback function returns zero,
