import ctypes
# Test ctypes.CFUNCTYPE

my_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
assert my_func(2) == 3

# my_func is a ctypes instance, but not a subclass of FunctionType
assert isinstance(my_func, ctypes.CFUNCTYPE)
assert not isinstance(my_func, FunctionType)
# Test ctypes.PYFUNCTYPE

try:
    ctypes.PYFUNCTYPE
except AttributeError:
    print("SKIP")
    raise SystemExit

my_func = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
assert my_func(2) == 3

# my_func is a ctypes instance, but not a subclass of FunctionType
assert isinstance(my_func, ctypes.PYFUNCTYPE)
assert not isinstance(my_func, FunctionType)
# Test ctypes.WINFUNCTYPE

try:

