import ctypes
# Test ctypes.CFUNCTYPE
#
# This test passes if it does not segfault.

def callback(x):
    print x
    return x

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(callback)
f(42)

ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))(f)
