import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The following function is used for testing. It is defined in
# _ctypes_test.c
#
# int call_int_callback(int(*func)(int)) {
#     return func(42);
# }

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print('callback called with', value)
    return value + 1

CALLBACKFUNC = CALLBACK(callback)

result = lib.call_int_callback(CALLBACKFUNC)
print('result', result)

#
# The following function is used for testing. It is defined in
# _ctypes_test.c
#
# int call_int_callback_i(int(*func)(int), int i) {
#     return func(i);
# }

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, c
