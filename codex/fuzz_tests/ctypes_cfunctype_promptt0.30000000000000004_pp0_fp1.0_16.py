import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    # Test ctypes.CFUNCTYPE
    #
    # ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
    #
    # Create a C callable function type, this is used to create
    # function prototypes.
    #
    # The first argument restype is the result type, followed by
    # zero or more argument types.  The result type and the argument
    # types may be any type, but are usually types created with
    # ctypes.CFUNCTYPE().
    #
    # If use_errno is True, a function is created that gets the
    # error code from the calling convention into ctypes.get_errno().
    #
    # If use_last_error is True, a function is created that gets the
    # error code from the calling convention into ctypes.get_last_error().
    #
    # The function created by ctypes.CFUNCTYPE() can be called
    # directly, or it can be
