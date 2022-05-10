import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print("callback called with", i)
    return 0

CALLBACK = FUNTYPE(my_callback)

dll = ctypes.CDLL("mylib.dll")
dll.set_callback(CALLBACK)
dll.call_callback()
</code>

