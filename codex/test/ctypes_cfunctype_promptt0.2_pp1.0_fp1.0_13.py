import ctypes
# Test ctypes.CFUNCTYPE

# Test ctypes.CFUNCTYPE(None)

import _ctypes_test

def func():
    pass

CALLBACK = ctypes.CFUNCTYPE(None)

# The callback is called, but the argument is ignored
