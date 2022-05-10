import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("Callback called with argument", arg)
    return 0

def register_callback(callback):
    func_ptr = FUNTYPE(callback)
    lib.register_callback(func_ptr)

register_callback(callback)

# call the callback
lib.call_callback()
</code>

