import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)
def func(a,b):
    print a,b
    r = ctypes.c_int(a+b)
    return r.value
f = FUNTYPE(func)
lib.test_callback(f)

def func(a,b,c):
    print a,b,c,"\n"
f = ctypes.WINFUNCTYPE(None,ctypes.c_int,ctypes.c_int,ctypes.c_int)(func)
lib.test_var_callback(f)
