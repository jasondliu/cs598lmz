import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

lib = ctypes.CDLL("./libmyfunc.so")
lib.myfunc.argtypes = (ctypes.c_int, FUNTYPE)

def my_callback(n):
    print(n[0])
    return 0

cb = FUNTYPE(my_callback)
lib.myfunc(4, cb)
