import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add_func(x, y):
    return x + y

lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.add.restype = ctypes.c_int
add_c = lib.add

cfunc = FUNTYPE(add_func)
lib.call_func.argtypes = (FUNTYPE, ctypes.c_int, ctypes.c_int)
lib.call_func.restype = ctypes.c_int
call_func = lib.call_func

print(add_c(1, 2))
print(call_func(cfunc, 1, 2))
