import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add(x, y):
    return x+y

add_f = FUNTYPE(add)

print add_f(1, 2)
