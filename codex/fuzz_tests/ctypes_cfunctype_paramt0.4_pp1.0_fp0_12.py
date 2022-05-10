import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print(a, b)
    return a + b

callback_func = FUNTYPE(callback)

lib = ctypes.CDLL('./libtest.so')
lib.test_callback(callback_func)
