import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    return x + y

callback = FUNTYPE(my_callback)

print(callback(1, 2))
</code>

