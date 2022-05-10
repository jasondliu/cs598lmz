import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def callback():
    print("hello")


callback_func = FUNTYPE(callback)

# C code
# typedef void (*callback_t)(void);
#
# callback_t func;
#
# void function()
# {
#     func();
# }

# lib = ctypes.CDLL("./libfunction.so")
lib = ctypes.CDLL("/Users/tracy/Documents/code/python/ctypes/function/libfunction.so")
lib.function.argtypes = []
lib.function.restype = None
lib.function.errcheck = None

lib.set_callback.argtypes = [FUNTYPE]
lib.set_callback.restype = None
lib.set_callback.errcheck = None

lib.set_callback(callback_func)
lib.function()
