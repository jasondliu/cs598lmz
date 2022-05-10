import ctypes
# Test ctypes.CFUNCTYPE
def call_int(fn, *args):
    c_int_p = ctypes.POINTER(ctypes.c_int)
    fn.restype = ctypes.c_int
    fn.argtypes = [c_int_p] + [ctypes.c_int] * len(args)
    result = ctypes.c_int()
    fn(ctypes.byref(result), *args)
    return result.value

def call_void(fn, *args):
    c_int_p = ctypes.POINTER(ctypes.c_int)
    fn.argtypes = [c_int_p] + [ctypes.c_int] * len(args)
    result = ctypes.c_int()
    fn(ctypes.byref(result), *args)

# Test ctypes.PYFUNCTYPE
def call_pyint(fn, *args):
    fn.restype = ctypes.c_int
    fn.argtypes = [ctypes.c_int] * len(args)
    return fn(*
