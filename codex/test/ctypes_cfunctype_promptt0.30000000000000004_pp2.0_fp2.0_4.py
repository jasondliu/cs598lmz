import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x

func_pointer = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
assert func_pointer(42) == 42

# Test ctypes.POINTER
func_pointer = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))(func_pointer)
assert func_pointer[0](42) == 42

# Test ctypes.byref
func_pointer = ctypes.byref(func_pointer)
