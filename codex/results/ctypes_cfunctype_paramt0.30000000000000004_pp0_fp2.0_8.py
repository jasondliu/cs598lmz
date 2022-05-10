import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print a, b
    return a + b

callback_func = FUNTYPE(callback)

lib.callback_func = callback_func

lib.call_callback(1, 2)
</code>

