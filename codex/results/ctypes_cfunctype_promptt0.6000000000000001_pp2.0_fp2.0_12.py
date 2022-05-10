import ctypes
# Test ctypes.CFUNCTYPE
def myfunc(a, b):
    print(a, b)
    return a + b

myfunc_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(myfunc)
print(myfunc_ptr(1, 2))
# Test ctypes.FunctionType
def myfunc(a, b):
    print(a, b)
    return a + b

myfunc_ptr = ctypes.FunctionType(myfunc.__code__, {})(myfunc)
print(myfunc_ptr(1, 2))
# Test ctypes.PYFUNCTYPE
def myfunc(a, b):
    print(a, b)
    return a + b

myfunc_ptr = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(myfunc)
print(myfunc_ptr(1, 2))
# Test ctypes.addressof
def myfunc(a, b):
    print(a,
