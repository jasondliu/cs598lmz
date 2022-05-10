import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print(x)
    return x

f = FUNTYPE(callback)
f(1)
</code>

