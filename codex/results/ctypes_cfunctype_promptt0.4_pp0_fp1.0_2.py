import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print(args)
    return args[-1]

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

_ctypes_test.set_callback(callback)

print(_ctypes_test.callback_i_iii(1, 2, 3))
print(_ctypes_test.callback_i_iii(4, 5, 6))

callback = CALLBACK(lambda *args: args[-1])

_ctypes_test.set_callback(callback)

print(_ctypes_test.callback_i_iii(1, 2, 3))
print(_ctypes_test.callback_i_iii(4, 5, 6))


# Test ctypes.WINFUNCTYPE

CALLBACK = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(
