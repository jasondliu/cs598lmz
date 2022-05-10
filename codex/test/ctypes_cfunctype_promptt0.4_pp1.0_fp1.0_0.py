import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p

# This is the prototype of the function we want to call
PROTO = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)

# This is the function we want to call
