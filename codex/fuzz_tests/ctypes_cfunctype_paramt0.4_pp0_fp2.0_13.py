import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

cfunc = FUNTYPE(my_callback)

# Calling the callback directly:
res = cfunc(1, 2)
print("my_callback returned %d" % res)

# Calling the callback from C:
lib.call_my_callback(cfunc, 3, 4)
</code>
Output:
<code>my_callback called with 1 and 2
my_callback returned 3
my_callback called with 3 and 4
</code>

