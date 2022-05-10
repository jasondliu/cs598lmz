import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def _callback(x):
    print(x)
    return x

_callback_ptr = FUNTYPE(_callback)

def callback(x):
    return _callback_ptr(x)

# Now, we can call callback from C
</code>

