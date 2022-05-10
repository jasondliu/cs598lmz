import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit of a hack, because we don't have a way to
# actually call the function pointer.  But at least we can check
# that the ctypes.CFUNCTYPE() function exists.

try:
    ctypes.CFUNCTYPE
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test ctypes.POINTER(ctypes.c_int)
#
# This test is a bit of a hack, because we don't have a way to
# actually call the function pointer.  But at least we can check
# that the ctypes.POINTER() function exists.

try:
    ctypes.POINTER
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test ctypes.Structure
#
# This test is a bit of a hack, because we don't have a way to
# actually call the function pointer.  But at least we can check
# that the ctypes.Structure() function exists.

try:
    ctypes.Structure
except AttributeError:

