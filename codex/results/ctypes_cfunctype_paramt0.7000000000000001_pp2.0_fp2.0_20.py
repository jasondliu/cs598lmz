import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
def cb_func(n):
    print("cb_func called with %d" % n)
    return 0

cb_func_ptr = FUNTYPE(cb_func)
lib.SetCallback(cb_func_ptr)

lib.CallCallback(42)

print("main complete")
</code>

