import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("callback called with %d and %d" % (a, b))
    return a + b

cbfunc = FUNTYPE(my_callback)

lib.call_func(5, 6, cbfunc)
</code>

