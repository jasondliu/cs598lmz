import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)
def func(arg1, arg2):
    return "Hello %d" % arg2

