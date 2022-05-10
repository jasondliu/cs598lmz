import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

cfunc = FUNTYPE(func)
print(cfunc(1))

# ctypes.c_int.from_address(id(cfunc))

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value

# ctypes.cast(cfunc, ctypes.c_void_p).value


