import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print "callback called with", x
    return x + 1

cb = FUNTYPE(callback)

print cb(1)
</code>
The output is:
<code>callback called with 1
2
</code>

