import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 5
assert fun() == 5
# the following is illegal, so we need macros
# funcptr = ctypes.cast(fun, ctypes.c_void_p)

