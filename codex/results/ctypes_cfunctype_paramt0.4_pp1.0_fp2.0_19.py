import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print("callback called with %d and %d" % (a, b))
    return a + b

cb = FUNTYPE(callback)

lib = ctypes.CDLL("./libtest.so")
lib.call_me_back(cb)
</code>
The output is:
<code>callback called with 1 and 2
callback called with 3 and 4
callback called with 5 and 6
callback called with 7 and 8
callback called with 9 and 10
</code>

