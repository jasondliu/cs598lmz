import ctypes
# Test ctypes.CFUNCTYPE()
# (the function to be called is not really called here)
#
# This example is based on one from www.python.org/doc/2.2.3/lib/ctypes-function-prototypes.html
#
# The ctypes prototype is of the form:
#   CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# where
#   restype is the result type
#   argtypes is a sequence of argument types
#   the use_errno and use_last_error args default to False
#
# The function prototype returned is of the form:
#   CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)(callable, <type 'method'>)(*argtypes)
# where
#   callable is the function to be called
#   restype, argtypes, use_errno, use_last_error are as above

import ctypes
import ctypes.util

# Obtain the function prototype
#
# We need to
