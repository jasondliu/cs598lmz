import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
def my_cb(arg):
    print("callback called with arg {}".format(arg))
    return 0

cb_obj = FUNTYPE(my_cb)
</code>
I don't know if this is the right way to do it, but it seems to work.

