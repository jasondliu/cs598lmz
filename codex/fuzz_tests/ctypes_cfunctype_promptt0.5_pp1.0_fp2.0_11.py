import ctypes
# Test ctypes.CFUNCTYPE()
def func(x, y):
    return x + y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(1, 2)

f = CMPFUNC(lambda x, y: x - y)
print f(1, 2)

# Test ctypes.PYFUNCTYPE()
def func(x, y):
    return x + y

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CMPFUNC(func)
print f(1, 2)

f = CMPFUNC(lambda x, y: x - y)
print f(1, 2)
