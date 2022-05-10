import ctypes
# Test ctypes.CFUNCTYPE for function pointers
# which require parameters
make_pointer = ctypes.CFUNCTYPE(
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)
# Prepare C interface
