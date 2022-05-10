import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback({}, {})".format(a, b))
    return a + b

c_callback = FUNTYPE(my_callback)

lib = ctypes.cdll.LoadLibrary("./libmy_callback.so")
lib.set_callback(c_callback)

lib.call_callback(1, 2)
</code>

