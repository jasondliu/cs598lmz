import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.POINTER, ctypes.c_void_p

libc = ctypes.CDLL(None)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
paramflags = (1, "arg1", 0),

# def myfunc(arg1):
#    return arg1

