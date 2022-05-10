import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

@jit
def fun_call(n):
    return sum(fun() for i in range(n))
