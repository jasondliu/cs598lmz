import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print("hello", i)
    return i

cb = FUNTYPE(callback)

mydll.myfunc(cb)

print("done")
</code>

