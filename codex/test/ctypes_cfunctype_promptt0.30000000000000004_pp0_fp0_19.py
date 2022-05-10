import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    print(a, b)

# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: The result type.
# argtypes: The argument types.
# use_errno: If True, and the function returns -1, ctypes will check errno
#            and raise an exception.
# use_last_error: If True, and the function returns -1, ctypes will check
#                 GetLastError() and raise an exception.

# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: The result type.
# argtypes: The argument types.
# use_errno: If True, and the function returns -1, ctypes will check errno
#            and raise an exception.
# use_last_error: If True, and the function returns -1, ctypes will check
#                 GetLastError() and raise an exception.

# CFUN
