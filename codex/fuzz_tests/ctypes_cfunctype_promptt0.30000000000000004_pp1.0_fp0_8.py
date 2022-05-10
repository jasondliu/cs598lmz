import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

# int func(int, int)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print("py_cmp_func(%d, %d)" % (a, b))
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

print(cmp_func(1, 2))
print(cmp_func(2, 1))

# int func(const void *, const void *)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

def py_cmp_func(a, b):
    a = ctypes.cast(a, ctypes.POINTER(ctypes.c_int))
    b = ctypes.cast(b, ctypes.POINTER(ctypes.c_int))
    print("py_cmp_
