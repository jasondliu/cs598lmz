import ctypes
# Test ctypes.CFUNCTYPE

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
#     Creates and returns a callable C function object.
#     The restype and argtypes are as for CFUNCTYPE().
#     If use_errno is True, the function will check for
#     errors after calling the function, and raise an
#     OSError exception if one was set.
#     If use_last_error is True, the function will check for
#     errors after calling the function, and raise a WindowsError
#     exception if one was set.
#     use_errno and use_last_error cannot both be True.

import _ctypes_test

def check_errno(result, func, arguments):
    if result == -1:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return result

def check_last_error(result, func, arguments):
    if result == 0
