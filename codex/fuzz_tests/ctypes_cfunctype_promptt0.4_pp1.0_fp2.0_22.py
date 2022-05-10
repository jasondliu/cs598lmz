import ctypes
# Test ctypes.CFUNCTYPE

def func(x, y):
    print("func", x, y)
    return x + y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(2, 3))

print(cmp_func.__name__)
print(cmp_func.__qualname__)
print(cmp_func.__module__)
print(cmp_func.__doc__)

print(cmp_func.__dict__)
print(cmp_func.__class__)

print(cmp_func.__annotations__)

# Test ctypes.PYFUNCTYPE

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(2, 3))

print(cmp_func.__name
