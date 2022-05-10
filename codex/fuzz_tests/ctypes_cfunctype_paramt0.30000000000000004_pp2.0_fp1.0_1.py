import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x

f = FUNTYPE(myfunc)
print(f(5))

# Python 2.6+
import ctypes

def myfunc(x):
    return x

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(myfunc)
print(f(5))
</code>

