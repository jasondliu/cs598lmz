import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    # ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
    # restype: the result type
    # argtypes: a sequence specifying the argument types
    # use_errno: if True, the function will check for the presence of errno
    # use_last_error: if True, the function will check for the presence of GetLastError()
    #
    # The function returns a callable object that when called invokes the function
    # pointed to by the function pointer.
    #
    # The callable object has the following attributes:
    # argtypes: a tuple of the argument types
    # restype: the result type
    # errcheck: a callable that is called with the result of the function
    #           and can raise an exception
    #
    # The callable object can be called with a variable number of arguments.
    #
    # The callable object can be passed to the following functions:
    # ctypes.windll.kernel32.SetWindowsH
