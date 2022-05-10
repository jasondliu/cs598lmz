import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

def callback(val):
    print("callback called with value:",val)
    return val

cb = FUNTYPE(callback)

lib = ctypes.CDLL("./libtest.so")
lib.test(cb)
</code>
Output:
<code>callback called with value: 5
</code>

