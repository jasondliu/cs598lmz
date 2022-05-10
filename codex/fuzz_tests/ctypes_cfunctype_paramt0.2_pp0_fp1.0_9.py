import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print("callback called with", x)
    return x

cbfunc = FUNTYPE(callback)

lib.callback(cbfunc)
</code>

