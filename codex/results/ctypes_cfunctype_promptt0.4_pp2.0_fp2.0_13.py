import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

func_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
func_c(1, 2)

# Test ctypes.POINTER

def func(a, b):
    return a + b

func_c = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))(func)
func_c(1, 2)

# Test ctypes.cast

def func(a, b):
    return a + b

func_c = ctypes.cast(func, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))
func_c(1, 2)

# Test ctypes.byref

def func(a, b):
    return a + b

func_c = ctypes.byref(ctypes.CF
