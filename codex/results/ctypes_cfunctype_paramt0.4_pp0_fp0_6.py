import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(a):
    print("in python callback", a)
    return 0

callback = FUNTYPE(my_callback)

dll.set_callback(callback)
dll.call_callback()
</code>

