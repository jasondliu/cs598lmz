import ctypes
# Test ctypes.CFUNCTYPE

# Here's a C function
# int varargs_func(int format, ...) { ... }

# We need to tell ctypes how a variable number of arguments is passed
# in C. This information varies from platform to platform, so
# ctypes uses a callback function to determine the correct argument
# passing mechanism.

