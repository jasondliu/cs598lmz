import ctypes
# Test ctypes.CFUNCTYPE

# Declare callback function
# This is the signature that must match the callback function
CB_FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Declare a variable for the callback function
cb_func = CB_FUNC()

# Declare a variable for the library handle
