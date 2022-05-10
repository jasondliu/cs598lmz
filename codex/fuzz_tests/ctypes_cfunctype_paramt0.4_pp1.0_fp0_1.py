import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print(x)
    return 0

callback_func = FUNTYPE(callback)

lib.test_callback(callback_func)
</code>

