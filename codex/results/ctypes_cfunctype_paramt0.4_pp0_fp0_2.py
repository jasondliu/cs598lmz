import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def register_callback(func):
    return FUNTYPE(func)

def callback(a, b):
    print("Called back with {} and {}".format(a, b))
    return a + b

# Register the callback
cb = register_callback(callback)

# Call the callback
cb(2, 3)

# Call the callback from C
lib.call_callback(cb)
</code>
Output:
<code>Called back with 2 and 3
Called back with 4 and 5
</code>

