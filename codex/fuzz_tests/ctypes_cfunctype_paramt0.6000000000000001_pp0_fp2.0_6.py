import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print x
    return x*x

f = FUNTYPE(callback)
print f(3)
</code>
output:
<code>3
9
</code>

