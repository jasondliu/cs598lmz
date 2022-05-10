import ctypes
# Test ctypes.CFUNCTYPE

int = ctypes.c_int
#@ctypes.CFUNCTYPE(int, int, int)
def func(a, b):
    return a + b

func.argtypes = [int, int]
func.restype = int

