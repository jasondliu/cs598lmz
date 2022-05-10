import ctypes
# Test ctypes.CFUNCTYPE

my_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
assert my_func(2) == 3

# my_func is a ctypes instance, but not a subclass of FunctionType
