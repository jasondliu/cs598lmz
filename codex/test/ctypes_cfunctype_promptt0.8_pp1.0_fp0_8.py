import ctypes
# Test ctypes.CFUNCTYPE
libc = ctypes.CDLL('libc.so.6')
time_t = ctypes.c_long

@ctypes.CFUNCTYPE(ctypes.c_long)
def c_time(time_t):
    return time_t

c_time.argtypes = time_t,
c_time.restype = time_t

res = c_time(libc.time(None))
