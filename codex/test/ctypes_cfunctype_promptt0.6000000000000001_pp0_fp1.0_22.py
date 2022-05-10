import ctypes
# Test ctypes.CFUNCTYPE()

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
def func(arg):
    print(arg[0])
    return 0

