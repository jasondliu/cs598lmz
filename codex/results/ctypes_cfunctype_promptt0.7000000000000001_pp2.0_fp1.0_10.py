import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    print("func")
    return a + b

# Callable prototype: int(int, int)
CFUNCTYPE(ctypes.c_int)(func)(2, 3)

# Callable prototype: int(int, int)
func_ptr = CFUNCTYPE(ctypes.c_int)(func)

func_ptr(2, 3)
# Test [ctypes.c_int, ctypes.c_int]
ctypes.c_int(2).value + ctypes.c_int(3).value
# Test [ctypes.c_int, ctypes.c_int]
a = ctypes.c_int(2)
b = ctypes.c_int(3)
a.value + b.value
# Test [ctypes.c_int, ctypes.c_int] ctypes.byref
ctypes.c_int(2).value + ctypes.c_int(3).value

a = ctypes.c_int(2)
b = ctypes.c_int(3
