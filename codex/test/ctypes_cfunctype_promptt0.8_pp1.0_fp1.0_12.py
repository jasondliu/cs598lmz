import ctypes
# Test ctypes.CFUNCTYPE

# prototypes of the functions we want to call
prototype = ctypes.CFUNCTYPE (ctypes.c_int, ctypes.c_int)

# list of the parameters we want to pass
params = (ctypes.c_int,)

