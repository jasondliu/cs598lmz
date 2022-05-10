import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(arg1, arg2):
    print("callback called %d, %d" % (arg1, arg2))
    return 0

cb = FUNTYPE(callback)

lib.test(cb)
</code>

