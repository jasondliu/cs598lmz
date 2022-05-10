import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)

def callback_func(val):
    print val
    time.sleep(0.05)
    return val

# Get (or create) a pointer to a function that matches FUNTYPE args and return
callback = FUNTYPE(callback_func)

# Register the callback to mymodule
# err = handle.register_callback(callback, 0)

while True:
    err = handle.register_callback(callback, 1)
    handle.unregister_callback(0)
    time.sleep(0.1)


lib.mymodule_destroy(handle)
