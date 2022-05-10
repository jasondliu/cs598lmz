import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x*2

f = FUNTYPE(myfunc)
print f(2)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
# ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# ctypes.c_int(1)
# ctypes.c_int(1).value
# ctypes.c_int(1).value + 1
# ctypes.c_int(1).value + 1 == 2
# ctypes.c_int(1).value + 1 == 3

# ctypes.c_int(1).value
# ctypes.c_int(1).value + 1
# ctypes.c_int(1).value + 1 == 2
# ctypes.
