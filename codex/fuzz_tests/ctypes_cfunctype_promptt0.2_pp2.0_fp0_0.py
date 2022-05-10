import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is the prototype of the callback function.
# It takes an integer argument and returns nothing.
CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

# This is the function that will be called from C.
def py_callback(arg):
    print("Callback called with argument %d" % arg)

# This is the C function that will call the callback.
# It takes a function pointer as first argument.
_c_callback = ctypes.CDLL(None).c_callback
_c_callback.argtypes = [CALLBACKFUNC]
_c_callback.restype = None

# Convert the Python function into a function pointer.
c_callback_func = CALLBACKFUNC(py_callback)

# Call the C function.
_c_callback(c_callback_func)

# Call the C function again.
_c_callback(c_callback_func)

# Call the C function with a different Python function.
_c_callback(CALLBACKFUNC(lambda arg: print
