import ctypes
# Test ctypes.CFUNCTYPE

int = ctypes.c_int
#@ctypes.CFUNCTYPE(int, int, int)
def func(a, b):
    return a + b

func.argtypes = [int, int]
func.restype = int

print func(1, 2)
print func(1, "2")

func_ptr = ctypes.cast(func, ctypes.c_void_p)
print func_ptr
