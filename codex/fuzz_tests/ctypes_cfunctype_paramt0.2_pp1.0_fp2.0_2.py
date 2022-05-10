import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)

def callback(x):
    print("callback called with", x)

cb = FUNTYPE(callback)

lib.call_callback(cb)
</code>

