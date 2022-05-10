import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit tricky, because we want to test that the
# ctypes.CFUNCTYPE() function returns a callable object, but we
# don't want to call the object, because it will crash the Python
# interpreter.  So we use the id() function to get the object's
# address, and then we compare the address with a known value.

# The known value is the address of the CFUNCTYPE() function.
# This is a bit of a hack, but it works.

# This test is a bit tricky, because we want to test that the
# ctypes.CFUNCTYPE() function returns a callable object, but we
# don't want to call the object, because it will crash the Python
# interpreter.  So we use the id() function to get the object's
# address, and then we compare the address with a known value.

# The known value is the address of the CFUNCTYPE() function.
# This is a bit of a hack, but it works.

import ctypes

if id(ctypes.CFUNCTYPE
