import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print("callback called with", n)
    return n * 2

cb = FUNTYPE(callback)

lib.call_callback(cb, 5)
</code>
Output:
<code>callback called with 5
</code>

