import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def _callback(arg1, arg2):
    print(arg1, arg2)
    return 0

callback = FUNTYPE(_callback)

dll.set_callback(callback)
dll.test_callback(1, 2)
</code>

