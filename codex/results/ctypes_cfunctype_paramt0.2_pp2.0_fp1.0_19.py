import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print("my_callback called with %d, %d" % (x, y))
    return x + y

lib = ctypes.CDLL("libmylib.so")
lib.register_callback(FUNTYPE(my_callback))
lib.run_callback(1, 2)
</code>

