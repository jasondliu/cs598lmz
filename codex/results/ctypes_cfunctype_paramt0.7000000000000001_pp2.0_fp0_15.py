import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b):
    print(a + b)
    return a + b
pfunc = FUNTYPE(func)
print(pfunc(10, 20))
print(pfunc)

print()
import ctypes
def func(a, b, c):
    print(a + b + c)
    return a + b + c
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
pfunc = FUNTYPE(func)
print(pfunc(10, 20, 30))
print(pfunc)

print()
import ctypes
def func(a, b, c):
    print(a + b + c)
    return a + b + c
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
pfunc = FUNTYPE
