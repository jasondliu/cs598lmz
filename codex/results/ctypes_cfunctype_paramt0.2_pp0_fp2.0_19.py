import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print 'got', a, b
    return a + b

callback = FUNTYPE(my_callback)

lib.call_me_back(callback)
</code>

