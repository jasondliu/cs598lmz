import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x + 1

cfunc = FUNTYPE(myfunc)
print(cfunc(1))

def myfunc2(x):
    return x + 2

cfunc2 = FUNTYPE(myfunc2)
print(cfunc2(1))

print(cfunc(1))
