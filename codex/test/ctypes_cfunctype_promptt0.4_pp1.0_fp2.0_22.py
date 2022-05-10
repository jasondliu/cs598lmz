import ctypes
# Test ctypes.CFUNCTYPE

def func(x, y):
    print("func", x, y)
    return x + y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(2, 3))

