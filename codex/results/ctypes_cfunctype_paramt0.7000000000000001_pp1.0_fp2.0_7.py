import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def c_callback(c_str):
    print c_str
    return 0

c_callback = FUNTYPE(c_callback)

lib.c_callback_func(c_callback)
</code>

