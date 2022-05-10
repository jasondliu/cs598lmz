import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2, 3)
fun.func_code = ctypes.cast(fun.__code__, ctypes.py_object)
fun.func_code.co_consts = (1, 2, 3)
</code>

