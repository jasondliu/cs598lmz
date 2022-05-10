import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print x
    return x

def callback2(x):
    print x
    return x

cb1 = FUNTYPE(callback)
cb2 = FUNTYPE(callback2)

lib.set_callback(cb1)
lib.set_callback(cb2)

lib.call_callback(3)
</code>
Output:
<code>3
3
</code>

