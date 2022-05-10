import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

c_t = _ctypes_test.getfunc(b'c_t')

def callback(*args):
    print('callback', args)
    return 1

f = c_t(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(callback))
print(f(1, 2))
