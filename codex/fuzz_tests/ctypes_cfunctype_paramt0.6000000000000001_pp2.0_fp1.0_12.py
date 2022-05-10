import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python:", a, b
    return a + b

CALLBACK = FUNTYPE(my_callback)
lib.register_callback(CALLBACK)
print lib.call_my_callback(1, 2)
</code>
Output:
<code>in python: 1 2
3
</code>

