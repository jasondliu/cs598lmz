import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    print("myfunc(%d) called" % x)
    return x

myfunc_c = FUNTYPE(myfunc)
myfunc_c(5)
</code>
This prints:
<code>myfunc(5) called
</code>

