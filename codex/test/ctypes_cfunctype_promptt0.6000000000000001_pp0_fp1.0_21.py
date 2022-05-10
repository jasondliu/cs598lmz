import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_void_p, ctypes.POINTER, ctypes.byref(),
# ctypes.cast()

# Test if ctypes can be used to call a C callback function from Python.
# The callback function is called from C, and returns a value.
# The callback function is passed a pointer to a structure.

import _ctypes_test

