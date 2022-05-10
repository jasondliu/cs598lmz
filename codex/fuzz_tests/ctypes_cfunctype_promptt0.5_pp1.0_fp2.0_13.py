import ctypes
# Test ctypes.CFUNCTYPE()

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
assert f(42) == 43
assert f.__name__ == 'func'

try:
    f.argtypes = [ctypes.c_int, ctypes.c_int]
except AttributeError:
    pass
else:
    raise Exception("shouldn't be able to set argtypes")

try:
    f.restype = ctypes.c_int
except AttributeError:
    pass
else:
    raise Exception("shouldn't be able to set restype")

# Test ctypes.PYFUNCTYPE()

def func(x):
    return x + 1

f = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
assert f(42) == 43
assert f.__name__ == 'func'

try:
    f.argtypes = [ctypes.c_int, c
