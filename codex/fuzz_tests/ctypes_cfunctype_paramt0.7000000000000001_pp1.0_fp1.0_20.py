import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)

def ft(n):
    print('callback called with', n)

cb = FUNTYPE(ft)
cb(10)
</code>

