import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(x, y):
    print(x, y)
    return x + y

c_callback = FUNTYPE(my_callback)

lib = ctypes.CDLL('./libfoo.so')
lib.foo(c_callback)
</code>

