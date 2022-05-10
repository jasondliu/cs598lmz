import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print("my_callback called with %d, %d" % (x, y))
    return x + y

my_callback_c = FUNTYPE(my_callback)

lib = ctypes.cdll.LoadLibrary("./libmylib.so")
lib.my_function.argtypes = (FUNTYPE, ctypes.c_int, ctypes.c_int)
lib.my_function.restype = ctypes.c_int

print("result: %d" % lib.my_function(my_callback_c, 1, 2))
</code>

