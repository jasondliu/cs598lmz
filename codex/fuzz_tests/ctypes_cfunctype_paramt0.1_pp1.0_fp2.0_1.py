import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    print("myfunc called with", x)
    return x

f = FUNTYPE(myfunc)
f(42)

# The following is equivalent to the above:
f = FUNTYPE(lambda x: x)
f(42)
</code>

