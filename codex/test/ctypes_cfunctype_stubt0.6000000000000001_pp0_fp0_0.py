import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

assert fun() == 42

# Issue #3075
c_int_p = ctypes.POINTER(ctypes.c_int)
c_int_p_p = ctypes.POINTER(c_int_p)
