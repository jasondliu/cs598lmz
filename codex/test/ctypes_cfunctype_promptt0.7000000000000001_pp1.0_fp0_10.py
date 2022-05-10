import ctypes
# Test ctypes.CFUNCTYPE
def f(x, y):
    return x + y
CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFunc(f)
print(cfunc(1, 2))
print(type(cfunc))

CFunc = ctypes.CFUNCTYPE(None, ctypes.c_int)
cfunc = CFunc(lambda x: print(x))
cfunc(1)

CFunc = ctypes.CFUNCTYPE(None)
f = CFunc(lambda: print('hello'))
f()

ctypes.c_int().value = 3
print(ctypes.c_int().value)

# Test ctypes.POINTER()
def f(x, y):
    return x + y
CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFunc(f)

ptr = ctypes.POINTER(CFunc)

