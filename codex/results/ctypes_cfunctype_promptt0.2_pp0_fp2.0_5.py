import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The following line is needed to make the test work on Windows.
# Without it, the function pointer is not correctly initialized.
lib.set_callback.restype = ctypes.c_int

# This callback is called from C, and must not raise an exception.
# The exception is printed, but not propagated to the caller.
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback(arg):
    print('callback called with', arg)
    if arg == 42:
        raise ValueError("don't panic")
    return arg + 1

lib.set_callback(callback)

# This callback is called from C, and must not raise an exception.
# The exception is printed, but not propagated to the caller.
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback_errcheck(result, func, arg):
    print('callback_err
