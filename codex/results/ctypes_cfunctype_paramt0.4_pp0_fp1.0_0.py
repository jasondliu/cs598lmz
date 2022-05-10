import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

@FUNTYPE
def callback(string):
    print string

lib.register_callback(callback)
</code>

