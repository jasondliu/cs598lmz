import ctypes
# Test ctypes.CFUNCTYPE() objects.  These are a bit different
# because the argtypes are not stored as a tuple, but in a separate
# list.  This means that we need to use another strategy to check that
# they work as expected.
#
