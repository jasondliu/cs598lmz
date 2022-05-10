import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print("x =", x)
    print("y =", y)
    return x + y

callback = FUNTYPE(callback)

lib.callback(callback)
</code>

