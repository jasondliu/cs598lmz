import ctypes
# Test ctypes.CFUNCTYPE
#
# This tests that the CFUNCTYPE() function can be used to create
# function prototypes for callback functions.
#
# The CFUNCTYPE() function takes the following arguments:
#
#  - The result type.
#  - A tuple of argument types.
#  - An optional keyword argument 'use_errno' which specifies whether
#    or not the calling function will set the C errno variable.
#  - An optional keyword argument 'use_last_error' which specifies
#    whether or not the calling function will set the Win32 last error
#    variable.
#
# The CFUNCTYPE() function returns a prototype object, which can be
# called with an integer address to create a callable object.
#
# The callable objects created by the prototype can be called just like
# a regular Python function.  They can also be passed to a C function
# expecting the corresponding C callback function type.
#
# When called, the Python function is passed one argument for each
# parameter declared in the callback prototype.  The parameters are
# passed as Python objects, and are converted from C
