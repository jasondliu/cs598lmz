import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(a, b):
    return a+b

callback = FUNTYPE(my_callback)
print(callback(2, 3))

# ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# ctypes.c_int
# ctypes.c_int
# ctypes.c_int

# ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# ctypes.c_int
# ctypes.c_int
# ctypes.c_int

# ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# ctypes.c_int
# ctypes.c_int
# ctypes.c_int

# ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, c
