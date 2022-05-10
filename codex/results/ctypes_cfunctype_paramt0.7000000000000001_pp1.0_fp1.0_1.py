import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
FUNC = FUNTYPE(add_native)
assert FUNC(1.0) == 2.0

def add_numpy(x):
    return x + 1

FUNC = FUNTYPE(add_numpy)
assert FUNC(1.0) == 2.0
</code>

