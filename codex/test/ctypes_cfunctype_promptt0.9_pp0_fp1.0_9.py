import ctypes
# Test ctypes.CFUNCTYPE().
cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def cdecl_callback(arg):
    return arg
def stdcall_callback(arg):
    return arg
cdecl = cf(cdecl_callback)
