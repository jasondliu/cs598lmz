import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print("callback called with", i)
    return 0

CALLBACK = FUNTYPE(my_callback)

lib.set_callback(CALLBACK)

lib.do_something(42)
