import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func_from_c(f):
    return FUNTYPE(f)

def func_from_py(f):
    return FUNTYPE(f)

def func_from_str(s):
    return FUNTYPE(s)
</code>

