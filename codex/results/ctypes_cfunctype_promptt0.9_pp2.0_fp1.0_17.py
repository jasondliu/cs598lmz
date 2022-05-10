import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test


lib = _ctypes_test.dll

################################################################
#
#      _ctypes_test.FUNC(arg) must be a function that calls
#      the function pointer passed with arg
#

def _func_callback(func, param):
    return func(param)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(_func_callback)
lib.set_callback(FUNC)

for i in range(10):
    r = lib.call_function_ptr(i)
    if r != i:
        print("Error when calling through function pointer:", r)
        raise Exception("Failed!")


################################################################

if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p):
    # Test sizeof(callback) and alignment
    # sizeof(callback) is 4 in 32bit and 8 in 64bit mode
    callback = ctypes.CFUNCTYPE(ctypes.c_int,
