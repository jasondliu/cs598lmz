import ctypes
# Test ctypes.CField instance
ctypes.c_int.in_dll(ctypes.CDLL(None), "errno")
PTR = ctypes.POINTER

libc = ctypes.CDLL(None)

class struct_timeval(ctypes.Structure):
    _fields_ = [
        ('tv_sec', ctypes.c_long),
        ('tv_usec', ctypes.c_long)
    ]

try:
    libc.select
except AttributeError:
    pass
else:
    libc.select.restype = ctypes.c_int
    libc.select.argtypes = [
        ctypes.c_int,
        PTR(ctypes.c_void_p),
        PTR(ctypes.c_void_p),
        PTR(ctypes.c_void_p),
        PTR(struct_timeval),
    ]
    libc.select.errcheck = lambda result, func, args: ctypes.get_errno()
    del libc  # Only want to test errcheck, so don't need
