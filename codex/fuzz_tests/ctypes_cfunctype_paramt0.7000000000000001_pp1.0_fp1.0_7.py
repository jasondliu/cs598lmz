import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def cb(data):
    print "cb", data
    return 0

CB = FUNTYPE(cb)

callback(CB, "something")
</code>
yields
<code>cb something
</code>

