import ctypes
# Test ctypes.CFUNCTYPE with ellipsis ('...', or 'args')
SIGNATURE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_char))
def func(s):
    return s[0]
F = SIGNATURE(func)
