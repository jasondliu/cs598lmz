import ctypes
# Test ctypes.CFUNCTYPE vs. ctypes.WINFUNCTYPE in py3.7
# The former is preferred. WINFUNCTYPE only works on Windows.

lib = ctypes.CDLL('libc.so.6')
calloc = lib.calloc
calloc.argtypes = [ctypes.c_size_t, ctypes.c_size_t]
calloc.restype = ctypes.c_void_p

# def cb(x=ctypes.POINTER(ctypes.c_long)):
#     print(x[0])
# cb_c = ctypes.CFUNCTYPE(ctypes.c_void_p)(cb)

# def cb(x=ctypes.c_long * 1):
#     print(x[0])
# cb_c = ctypes.CFUNCTYPE(ctypes.c_void_p)(cb)

def cb(x=ctypes.c_long):
    print(x)
