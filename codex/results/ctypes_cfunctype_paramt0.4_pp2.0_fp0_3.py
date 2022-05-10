import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def myfunc(a, b):
    return a + b

CMPFUNC = FUNTYPE(myfunc)
print CMPFUNC(1, 2)

# Python3
# FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# CMPFUNC = FUNTYPE(lambda a, b: a + b)
# print CMPFUNC(1, 2)

# Python3
# FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# CMPFUNC = FUNTYPE(lambda a, b: a + b)
# print CMPFUNC(1, 2)

# Python3
# FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# CMPFUNC = FUNTYPE(lambda a,
