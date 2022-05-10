import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

cfunc = FUNTYPE(func)
print cfunc(1, 2)

# ctypes.POINTER(ctypes.c_int)

# ctypes.c_int.in_dll(lib, 'a')

# ctypes.c_int.from_address(addressof(lib.a))

# ctypes.cast(addressof(lib.a), ctypes.POINTER(ctypes.c_int))

# ctypes.byref(lib.a)

# ctypes.c_void_p.in_dll(lib, 'a')

# ctypes.c_void_p.from_address(addressof(lib.a))

# ctypes.cast(addressof(lib.a), ctypes.POINTER(ctypes.c_void_p))

# ctypes.byref(lib.a)

# ctypes.c_int.in_
