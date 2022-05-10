import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print("callback", i)
    return i

CALLBACK = FUNTYPE(callback)

lib.call_me_back(CALLBACK)
</code>

