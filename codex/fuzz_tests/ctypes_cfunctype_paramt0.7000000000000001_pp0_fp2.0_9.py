import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

def callback(arg1, arg2):
    print("callback: arg1={0}, arg2={1}".format(arg1, arg2))

callback_func = FUNTYPE(callback)

lib.add_callback(callback_func)

# You can also add the callback in this way:
# lib.add_callback.argtypes = [FUNTYPE]
# lib.add_callback.restype = None
# lib.add_callback(callback_func)

lib.call_callback()
</code>

