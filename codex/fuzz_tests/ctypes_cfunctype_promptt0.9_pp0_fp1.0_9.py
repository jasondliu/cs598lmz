import ctypes
# Test ctypes.CFUNCTYPE().
cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def cdecl_callback(arg):
    return arg
def stdcall_callback(arg):
    return arg
cdecl = cf(cdecl_callback)
stdcall = cf(stdcall_callback, False) # last argument
try:
    fastcall_callback = None
except NameError: # no fastcall in cdecl mode
    fastcall = None
else:
    fastcall = cf(fastcall_callback, False, "fastcall")
