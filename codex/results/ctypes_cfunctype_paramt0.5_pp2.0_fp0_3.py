import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.POINTER(ctypes.c_int))

def register_callback(callback):
    global f
    f = FUNTYPE(callback)
    lib.register_callback(f)

def call_callback():
    lib.call_callback()

register_callback(callback)
call_callback()
lib.unregister_callback()
</code>

