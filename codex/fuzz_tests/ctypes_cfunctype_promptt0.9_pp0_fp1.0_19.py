import ctypes
# Test ctypes.CFUNCTYPE.

def c_callback(arg1, arg2, arg3):
    return arg1, arg2, arg3


CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

cb_func = CALLBACK(c_callback)
print repr(cb_func(1, 2, 3))

cp_func = ctypes.cast(cb_func, ctypes.c_void_p).value
print repr(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
                 (cp_func)(1, 2, 3))
