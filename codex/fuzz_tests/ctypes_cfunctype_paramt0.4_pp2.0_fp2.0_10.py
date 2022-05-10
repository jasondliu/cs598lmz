import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print(i)
    return i

cb = FUNTYPE(callback)

lib.call_me(cb)
</code>

