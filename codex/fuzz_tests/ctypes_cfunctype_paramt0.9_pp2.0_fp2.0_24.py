import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def use_old_callback(lib, callback):
    fun = FUNTYPE(callback)
    set_callback_a(lib, fun)
    print(lib.call_a(2.0))
use_old_callback(lib, callback)

def add_call_b(lib, callback):
    # https://docs.python.org/3/library/ctypes.html#mixing-in-c-types
    lib.call_b.argtypes = [FUNTYPE, ctypes.c_double]
    lib.call_b.restype = ctypes.c_double
    def cfunc(x):
        return lib.call_b(callback, x)
    return cfunc
cfunc = add_call_b(lib, callback)
print(cfunc(2.0))

@runtime_check
def callback_cfunc(x, y, z):
    if x > y:
        return 1.0
    else:
        return z

def newcallback(f, args):
   
