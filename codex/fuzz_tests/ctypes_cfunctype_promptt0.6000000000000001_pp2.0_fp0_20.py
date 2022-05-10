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
else:
    raise Exception("should have failed")

# But this should work
CFUNCTYPE2 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# This should fail
try:
    ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)
except TypeError:
    pass
else:
    raise Exception("should have failed")

# This should work
CFUNCTYPE3 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This should fail
try:
    c
