import ctypes
# Test ctypes.CFUNCTYPE
#
# We use the ctypes.CFUNCTYPE to wrap a simple C function that adds two
# integers.
#
# The function is created with the ctypes.CFUNCTYPE constructor and the
# ctypes.c_int32 type.
#
# The result is assigned to a variable called AddInts.
#
# The function is called by passing two integer arguments.
#
# The result is then printed.

# Import the ctypes library
import ctypes

# Load the shared library into ctypes
