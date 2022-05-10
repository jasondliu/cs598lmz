import ctypes
# Test ctypes.CFUNCTYPE
#
#    CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# Create function prototypes with prototype calling conventions.  The
# restype and argtypes can be any valid type.  See the standard ctypes
# documentation for more on these types.
#
# If restype is ctypes.c_void_p, the return value is converted to
# a Python object using the PyCObject API.
#
# If use_errno is True, the function will be passed -errno- as
# its last argument.  If the function returns 0, this will return
# the ctypes formatted version of errno.  Otherwise, the function
# will return the result of the function call.
#
# If use_last_error is True, the function will be passed -GetLastError()-
# as its last argument.  If the function returns 0, this will return
# the ctypes formatted version of GetLastError().  Otherwise, the
# function will return the result of the function call.
#
# Note: use_errno and
