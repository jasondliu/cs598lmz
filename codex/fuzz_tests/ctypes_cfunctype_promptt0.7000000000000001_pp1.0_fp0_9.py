import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 42)() == 42

# This test is for the bug reported in issue #1664.

import ctypes

DLL = ctypes.CDLL(ctypes.util.find_library("c"))

def callback(x):
    print('callback called')
    return x

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
CALLBACKFUNC(callback)

libc_callback = CALLBACKFUNC(DLL._testfunc_f_i)
libc_callback(42)
