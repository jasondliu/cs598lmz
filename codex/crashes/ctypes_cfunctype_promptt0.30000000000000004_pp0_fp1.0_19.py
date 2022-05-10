import ctypes
Callable = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func = Callable(42)
assert func(1) == 42
