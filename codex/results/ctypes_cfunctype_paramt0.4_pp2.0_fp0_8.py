import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback(n):
    print(n)
    return 0

f = FUNTYPE(callback)

lib.callback_func(f)
</code>

