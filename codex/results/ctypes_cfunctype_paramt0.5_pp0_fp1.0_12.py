import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(a, b):
    print("my_callback", a, b)
    return 42
c_callback = FUNTYPE(my_callback)

lib = ctypes.CDLL("./libmylib.so")
lib.set_callback(c_callback)

lib.call_callback(1, 2)
</code>

