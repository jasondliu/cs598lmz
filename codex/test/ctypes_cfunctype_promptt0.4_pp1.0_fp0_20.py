import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print('func', args)
    return args[-1]

CFUNCTYPE = ctypes.CFUNCTYPE

c_func = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

print(c_func(1, 2))
print(c_func(3, 4, 5))

c_func = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda *args: args[-1])
print(c_func(1, 2))
print(c_func(3, 4, 5))

c_func = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)
print(c_func(1, 2))
print(c_func(3, 4, 5))

