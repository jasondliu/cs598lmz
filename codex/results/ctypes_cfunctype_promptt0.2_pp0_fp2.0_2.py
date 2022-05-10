import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print func_ptr(1, 2)

func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda a, b: a + b)
print func_ptr(1, 2)

func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda a, b: a + b, ())
print func_ptr(1, 2)

func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda a, b: a + b, (1,))
print func_ptr(1, 2)

func_ptr = ctypes.CFUNCTYPE(ctypes.c_int,
