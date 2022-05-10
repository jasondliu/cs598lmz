import ctypes
# Test ctypes.CFUNCTYPE for multiple argument types

try:
    import _ctypes_test
except ImportError:
    import sys
    print('skipped')
    sys.exit()

# This should fail
try:
    ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
except TypeError:
    pass
