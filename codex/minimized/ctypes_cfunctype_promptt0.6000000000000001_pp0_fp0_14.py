import ctypes
def callback(n):
    return n * 2
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
CALLBACKP = ctypes.POINTER(CALLBACK)
c_callback = CALLBACK(callback)
c_callbackp = ctypes.cast(c_callback, CALLBACKP)
assert c_callbackp[0](41) == callback(41) == 82
